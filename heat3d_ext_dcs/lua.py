"""
A small, tolerant reader for the Lua that DCS World's database is written in.

It is not a Lua interpreter: it reads tables, numbers, strings and simple
arithmetic, follows assignments into a table of names, and walks a function's
body when the function is called - straight through, with `if` branches all
taken in order, a `for` loop repeated only over a table or range it knows
(at most MAX_LOOP times), and nothing but files inside the install read.
Anything it cannot know (a value from the game's own engine, a loop counter)
reads as `None`, or as a `Ref` naming the unknown thing, and is carried along.
The calls that declare things (`declare_weapon`, `declare_sensor`,
`add_aircraft`, ...) are handed to a hook so a caller can collect them.
"""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any, Callable

_TOKEN = re.compile(
    r"""
    (?P<ws>\s+)
  | (?P<lcomment>--\[(?P<lceq>=*)\[.*?\](?P=lceq)\])
  | (?P<comment>--[^\n]*)
  | (?P<lstr>\[(?P<lseq>=*)\[.*?\](?P=lseq)\])
  | (?P<num>0[xX][0-9a-fA-F]+|(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)
  | (?P<name>[A-Za-z_][A-Za-z0-9_]*)
  | (?P<str>"(?:[^"\\\n]|\\.|\\\n)*"|'(?:[^'\\\n]|\\.|\\\n)*')
  | (?P<op>\.\.\.|\.\.|==|~=|<=|>=|//|::|<<|>>|[-+*/%^\#&~|<>=(){}\[\];:,.])
    """,
    re.S | re.X,
)

KEYWORDS = {"and", "break", "do", "else", "elseif", "end", "false", "for", "function", "goto", "if", "in", "local",
            "nil", "not", "or", "repeat", "return", "then", "true", "until", "while"}

_ESC = {"n": "\n", "t": "\t", "r": "\r", "a": "\a", "b": "\b", "f": "\f", "v": "\v", "\\": "\\", '"': '"', "'": "'",
        "\n": "\n"}


def _unescape(s: str) -> str:
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c != "\\" or i + 1 >= len(s):
            out.append(c)
            i += 1
            continue
        n = s[i + 1]
        if n in _ESC:
            out.append(_ESC[n])
            i += 2
        elif n.isdigit():
            m = re.match(r"\d{1,3}", s[i + 1:])
            out.append(chr(int(m.group(0)) & 0xFF))
            i += 1 + len(m.group(0))
        elif n == "x":
            out.append(chr(int(s[i + 2:i + 4], 16)) if re.match(r"[0-9a-fA-F]{2}", s[i + 2:i + 4]) else "")
            i += 4
        elif n == "z":
            i += 2
            while i < len(s) and s[i].isspace():
                i += 1
        else:
            out.append(n)
            i += 2
    return "".join(out)


def tokenize(text: str) -> list[tuple[str, Any]]:
    """(kind, value) pairs: kind is 'num', 'str', 'name', 'kw' or 'op'."""
    out: list[tuple[str, Any]] = []
    pos = 0
    n = len(text)
    while pos < n:
        m = _TOKEN.match(text, pos)
        if m is None:  # a character Lua would reject: step over it
            pos += 1
            continue
        pos = m.end()
        k = m.lastgroup
        v = m.group(k)
        if k in ("ws", "comment", "lcomment"):
            continue
        if k in ("lceq", "lseq"):  # only inside their outer groups
            continue
        if k == "num":
            try:
                out.append(("num", int(v, 16) if v[:2] in ("0x", "0X") else (int(v) if v.isdigit() else float(v))))
            except ValueError:
                out.append(("num", None))
        elif k == "name":
            out.append(("kw" if v in KEYWORDS else "name", v))
        elif k == "str":
            out.append(("str", _unescape(v[1:-1])))
        elif k == "lstr":
            eq = len(m.group("lseq"))
            body = v[2 + eq:-(2 + eq)]
            out.append(("str", body[1:] if body.startswith("\n") else body))
        else:
            out.append(("op", v))
    return out


class Ref:
    """Something the reader cannot know, by the name it was reached through (e.g. `GT_t.LN_t.NASAMS`)."""

    __slots__ = ("path",)

    def __init__(self, path: str):
        self.path = path

    def __repr__(self) -> str:
        return f"Ref({self.path})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Ref) and other.path == self.path

    def __hash__(self) -> int:
        return hash(("Ref", self.path))


class LuaTable:
    __slots__ = ("h", "meta", "proto")

    def __init__(self):
        self.h: dict = {}
        self.meta: LuaTable | None = None  # the table missing fields are read from (a metatable's __index)
        self.proto: str | None = None  # the name of a prototype the reader could not see

    @staticmethod
    def key(k):
        if isinstance(k, float) and k.is_integer():
            return int(k)
        if isinstance(k, Ref):
            return k.path
        if isinstance(k, bool):
            return k
        return k

    def get(self, k, depth: int = 0):
        k = self.key(k)
        if k in self.h:
            v = self.h[k]
            if isinstance(v, LuaTable) and v.meta is None and self.meta is not None and depth < 20:
                mv = self.meta.peek(k, depth + 1)  # a recursive metatable reaches into sub-tables too
                if isinstance(mv, LuaTable) and mv is not v:
                    v.meta = mv
            return v
        if self.meta is not None and depth < 20:
            return self.meta.peek(k, depth + 1)
        return None

    def peek(self, k, depth: int = 0):
        """A field, through the metatable, without making anything (what a prototype lookup reads)."""
        return self.get(k, depth)

    def set(self, k, v) -> None:
        if k is None:
            return
        k = self.key(k)
        if isinstance(k, float) and math.isnan(k):
            return
        if v is None:
            self.h.pop(k, None)
        else:
            self.h[k] = v

    def array(self) -> list:
        out = []
        i = 1
        while True:
            v = self.get(i)
            if v is None:
                return out
            out.append(v)
            i += 1

    def keys(self) -> list:
        seen = list(self.h)
        if self.meta is not None:
            seen += [k for k in self.meta.keys() if k not in self.h]
        return seen

    def __repr__(self) -> str:
        return f"LuaTable({len(self.h)})"


class Namespace(LuaTable):
    """
    A table of the game's engine the reader cannot see (`GT_t`): reading a field
    that is not there makes an empty one with its name, so assignments into it
    land and a prototype it holds can still be named.
    """

    __slots__ = ("path",)

    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def get(self, k, depth: int = 0):
        k = self.key(k)
        if k is None:
            return None
        if k not in self.h:
            self.h[k] = Namespace(f"{self.path}.{k}")
        return self.h[k]

    def peek(self, k, depth: int = 0):
        return self.h.get(self.key(k))

    def array(self) -> list:
        out = []
        i = 1
        while i in self.h:
            out.append(self.h[i])
            i += 1
        return out

    def keys(self) -> list:
        return list(self.h)


class Func:
    __slots__ = ("params", "vararg", "start", "end", "scope", "chunk", "name")

    def __init__(self, params, vararg, start, end, scope, chunk, name=""):
        self.params, self.vararg, self.start, self.end, self.scope, self.chunk, self.name = (
            params, vararg, start, end, scope, chunk, name)


class Scope:
    __slots__ = ("vars", "parent", "varargs")

    def __init__(self, parent: "Scope | None" = None, varargs: list | None = None):
        self.vars: dict = {}
        self.parent = parent
        self.varargs = varargs or []

    def find(self, name: str) -> "Scope | None":
        s = self
        while s is not None:
            if name in s.vars:
                return s
            s = s.parent
        return None


class _Stop(Exception):
    pass


def truthy(v) -> bool:
    return v is not None and v is not False and not isinstance(v, Ref)


def number(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return v
    if isinstance(v, str):
        try:
            return float(v) if "." in v or "e" in v.lower() else int(v)
        except ValueError:
            return None
    return None


class Chunk:
    __slots__ = ("toks", "path")

    def __init__(self, toks, path):
        self.toks, self.path = toks, path


_BINARY = {
    "or": 1, "and": 2,
    "<": 3, ">": 3, "<=": 3, ">=": 3, "~=": 3, "==": 3,
    "|": 4, "~": 5, "&": 6, "<<": 7, ">>": 7, "..": 9,
    "+": 10, "-": 10, "*": 11, "/": 11, "//": 11, "%": 11, "^": 14,
}
_RIGHT = {"..": 8, "^": 13}  # right associative: the right side binds at this level
_UNARY = 12


class Reader:
    """
    Reads Lua files into one shared set of globals. `hooks` maps a function's
    last name (`declare_weapon`) to a Python callable taking the argument list.
    `root` bounds what `dofile` may read.
    """

    def __init__(self, root: Path | None = None, hooks: dict[str, Callable] | None = None, max_steps: int = 20_000_000):
        self.root = Path(root).resolve() if root else None
        self.globals = Scope()
        self.hooks = dict(hooks or {})
        self.steps = 0
        self.max_steps = max_steps
        self.depth = 0
        self.loaded: set[Path] = set()
        self.active: dict[int, int] = {}
        self.frozen: set[str] = set()  # globals the files may not overwrite
        self.errors: list[str] = []
        self.files_read = 0
        g = self.globals.vars
        mt = LuaTable()
        for k, f in {"rad": math.radians, "deg": math.degrees, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                     "sqrt": math.sqrt, "abs": abs, "floor": math.floor, "ceil": math.ceil, "exp": math.exp,
                     "atan": math.atan, "asin": math.asin, "acos": math.acos, "log": math.log}.items():
            mt.set(k, _builtin(f))
        mt.set("min", _builtin(min, many=True))
        mt.set("max", _builtin(max, many=True))
        mt.set("pi", math.pi)
        mt.set("huge", float("inf"))
        g["math"] = mt
        tt = LuaTable()
        tt.set("insert", self._table_insert)
        g["table"] = tt
        g["_"] = lambda a: a[0] if a else None
        g["tonumber"] = lambda a: number(a[0]) if a else None
        g["tostring"] = lambda a: (str(a[0]) if isinstance(a[0], (int, float, str)) else None) if a else None
        g["setmetatable"] = self._setmetatable
        g["set_recursive_metatable"] = self._set_recursive_metatable
        g["dofile"] = self._dofile
        g["loadfile"] = self._loadfile
        g["ipairs"] = g["pairs"] = g["unpack"] = g["type"] = g["print"] = g["require"] = lambda a: None

    # -- builtins -------------------------------------------------------

    @staticmethod
    def _table_insert(a):
        if a and isinstance(a[0], LuaTable):
            t = a[0]
            if len(a) >= 3 and isinstance(number(a[1]), (int, float)):
                pos = int(number(a[1]))
                items = t.array()
                items.insert(max(0, pos - 1), a[2])
                for i, v in enumerate(items, 1):
                    t.set(i, v)
            elif len(a) >= 2:
                t.set(len(t.array()) + 1, a[1])
        return None

    @staticmethod
    def _setmetatable(a):
        if len(a) >= 2 and isinstance(a[0], LuaTable) and isinstance(a[1], LuaTable):
            idx = a[1].get("__index")
            if isinstance(idx, LuaTable):
                a[0].meta = idx
        return a[0] if a else None

    @staticmethod
    def _set_recursive_metatable(a):
        if len(a) >= 2 and isinstance(a[0], LuaTable):
            if isinstance(a[1], LuaTable):
                a[0].meta = a[1]
            elif isinstance(a[1], Ref):
                a[0].proto = a[1].path
        return None

    def _resolve(self, p) -> Path | None:
        if not isinstance(p, str) or self.root is None:
            return None
        path = Path(p.replace("\\", "/"))
        if not path.is_absolute():
            path = self.root / path
        try:
            path = path.resolve()
        except OSError:
            return None
        if path != self.root and self.root not in path.parents:
            return None  # never outside the install
        return path if path.is_file() else None

    def _dofile(self, a):
        path = self._resolve(a[0] if a else None)
        if path is None:
            return None
        return self.run_file(path)

    def _loadfile(self, a):
        path = self._resolve(a[0] if a else None)
        if path is None:
            return None
        return lambda _args: self.run_file(path)

    # -- entry points ---------------------------------------------------

    def run_file(self, path: Path, once: bool = False):
        path = Path(path)
        try:
            key = path.resolve()
        except OSError:
            key = path
        if once and key in self.loaded:
            return None
        self.loaded.add(key)
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            self.errors.append(f"{path}: {e}")
            return None
        self.files_read += 1
        return self.run(text, str(path))

    def run(self, text: str, name: str = "<text>"):
        chunk = Chunk(tokenize(text), name)
        if self.depth > 40:
            return None
        self.depth += 1
        try:
            ret = _Exec(self, chunk, Scope(self.globals)).block(0, len(chunk.toks))
        except _Stop:
            ret = None
        finally:
            self.depth -= 1
        return ret

    def get(self, name: str):
        return self.globals.vars.get(name)

    def call(self, f, args: list):
        if isinstance(f, Func):
            if self.depth > 40 or self.active.get(id(f), 0) >= 2:
                return None  # recursion, walked straight through, would branch without end
            if _COPY.search(f.name or ""):
                return _copy_call(args)
            sc = Scope(f.scope, varargs=args[len(f.params):] if f.vararg else [])
            for i, p in enumerate(f.params):
                sc.vars[p] = args[i] if i < len(args) else None
            self.depth += 1
            self.active[id(f)] = self.active.get(id(f), 0) + 1
            try:
                return _Exec(self, f.chunk, sc).block(f.start, f.end)
            finally:
                self.depth -= 1
                self.active[id(f)] -= 1
        if callable(f):
            try:
                return f(args)
            except (TypeError, ValueError, ArithmeticError, OverflowError):
                return None
        return None


#: Helpers that copy tables with a loop over pairs(): the walk-through cannot run them, so they are done here.
_COPY = re.compile(r"copy", re.I)


def deepcopy(v, memo: dict | None = None):
    if not isinstance(v, LuaTable):
        return v
    memo = {} if memo is None else memo
    if id(v) in memo:
        return memo[id(v)]
    t = Namespace(v.path) if isinstance(v, Namespace) else LuaTable()
    memo[id(v)] = t
    t.meta, t.proto = v.meta, v.proto
    for k, x in v.h.items():
        t.h[k] = deepcopy(x, memo)
    return t


def _copy_call(args: list):
    """copy(src) returns a copy; copy(target, src) fills target from src and returns it."""
    if len(args) >= 2 and isinstance(args[0], LuaTable) and isinstance(args[1], LuaTable):
        for k, x in args[1].h.items():
            if isinstance(x, LuaTable) and isinstance(args[0].h.get(k), LuaTable):
                _copy_call([args[0].h[k], x])
            else:
                args[0].h[k] = deepcopy(x)
        return args[0]
    return deepcopy(args[0]) if args else None


def _builtin(f, many=False):
    def call(a):
        nums = [number(x) for x in a]
        if not nums or any(x is None for x in nums):
            return None
        return f(*nums) if many else f(nums[0])
    return call


class _ParseError(Exception):
    pass


class _Exec:
    """Walks the tokens of one chunk (or one function body) once, from start to end."""

    def __init__(self, reader: Reader, chunk: Chunk, scope: Scope):
        self.r = reader
        self.c = chunk
        self.t = chunk.toks
        self.scope = scope
        self.pos = 0
        self.end = 0

    # -- token helpers ----------------------------------------------------

    def peek(self, off: int = 0):
        i = self.pos + off
        return self.t[i] if i < self.end else ("eof", None)

    def at(self, kind: str, value=None, off: int = 0) -> bool:
        k, v = self.peek(off)
        return k == kind and (value is None or v == value)

    def take(self, kind: str, value=None):
        k, v = self.peek()
        if k != kind or (value is not None and v != value):
            raise _ParseError(f"expected {value or kind}, got {v!r}")
        self.pos += 1
        return v

    def skip_block(self) -> int:
        """From just after `function(...)`, the index of its matching `end`."""
        depth = 1
        i = self.pos
        while i < self.end:
            k, v = self.t[i]
            if k == "kw":
                if v in ("function", "do", "if"):
                    depth += 1
                elif v == "repeat":
                    depth += 1
                elif v in ("end", "until"):
                    depth -= 1
                    if depth == 0:
                        return i
            i += 1
        return self.end

    # -- statements ---------------------------------------------------------

    def block(self, start: int, end: int):
        self.pos, self.end = start, end
        ret = None
        while self.pos < self.end:
            self.r.steps += 1
            if self.r.steps > self.r.max_steps:
                raise _Stop()
            here = self.pos
            try:
                v = self.statement()
                if v is not None:
                    ret = v
                if self.pos == here:
                    self.pos += 1
            except _ParseError:
                self.pos = here + 1
            except RecursionError:
                self.pos = here + 1
        return ret

    def statement(self):
        k, v = self.peek()
        if k == "op" and v in (";", ")", "]", "}", ","):
            self.pos += 1
            return None
        if k == "op" and v == "::":
            self.pos += 3
            return None
        if k == "kw":
            if v in ("if", "elseif", "while", "until"):
                self.pos += 1
                self.expr()
                if self.at("kw", "then") or self.at("kw", "do"):
                    self.pos += 1
                return None
            if v in ("then", "else", "do", "end", "repeat", "break"):
                self.pos += 1
                return None
            if v == "goto":
                self.pos += 2
                return None
            if v == "for":
                self.pos += 1
                names = [self.take("name")]
                while self.at("op", ","):
                    self.pos += 1
                    names.append(self.take("name"))
                numeric = self.at("op", "=")
                over = None
                if numeric or self.at("kw", "in"):
                    self.pos += 1
                    if numeric:
                        over = self.exprlist()
                    elif self.at("name") and self.peek()[1] in ("ipairs", "pairs") and self.at("op", "(", 1):
                        fn = self.peek()[1]
                        self.pos += 2
                        over = (fn, self.expr())
                        self.take("op", ")")
                    else:
                        self.exprlist()
                for n in names:
                    self.scope.vars[n] = None
                if not self.at("kw", "do"):
                    return None
                self.pos += 1
                rows = _iterations(numeric, over)
                if rows is None:  # not known: walk the body once, straight through
                    return None
                start = self.pos
                end = self.skip_block()
                ret = None
                for row in rows:
                    for i, n in enumerate(names):
                        self.scope.vars[n] = row[i] if i < len(row) else None
                    v = _Exec(self.r, self.c, self.scope).block(start, end)
                    if v is not None:
                        ret = v
                self.pos = end + 1
                return ret
            if v == "return":
                self.pos += 1
                if self.at("eof") or (self.at("kw") and self.peek()[1] in ("end", "else", "elseif", "until")) or self.at("op", ";"):
                    return None
                vals = self.exprlist()
                return vals[0] if vals else None
            if v == "local":
                self.pos += 1
                if self.at("kw", "function"):
                    self.pos += 1
                    name = self.take("name")
                    self.scope.vars[name] = None
                    self.scope.vars[name] = self.funcbody(name)
                    return None
                names = [self.take("name")]
                self._attrib()
                while self.at("op", ","):
                    self.pos += 1
                    names.append(self.take("name"))
                    self._attrib()
                vals = []
                if self.at("op", "="):
                    self.pos += 1
                    vals = self.exprlist()
                for i, n in enumerate(names):
                    self.scope.vars[n] = vals[i] if i < len(vals) else None
                return None
            if v == "function":
                self.pos += 1
                path = [self.take("name")]
                method = False
                while self.at("op", ".") or self.at("op", ":"):
                    method = self.peek()[1] == ":"
                    self.pos += 1
                    path.append(self.take("name"))
                f = self.funcbody(".".join(path), self_param=method)
                if len(path) == 1:
                    self.assign_name(path[0], f)
                else:
                    t = self.lookup(path[0])
                    for p in path[1:-1]:
                        t = t.get(p) if isinstance(t, LuaTable) else None
                    if isinstance(t, LuaTable):
                        t.set(path[-1], f)
                return None
            # a stray keyword: step over it
            self.pos += 1
            return None
        # assignment or call
        targets = [self.suffixed(lvalue=True)]
        if self.at("op", "=") or self.at("op", ","):
            if targets[0] is None:
                raise _ParseError("not assignable")
            while self.at("op", ","):
                self.pos += 1
                targets.append(self.suffixed(lvalue=True))
            self.take("op", "=")
            if any(tg is None for tg in targets):
                raise _ParseError("not assignable")
            vals = self.exprlist()
            for i, tg in enumerate(targets):
                val = vals[i] if i < len(vals) else None
                if tg[0] == "name":
                    self.assign_name(tg[1], val)
                elif tg[0] == "index" and isinstance(tg[1], LuaTable):
                    tg[1].set(tg[2], val)
            return None
        return None

    def _attrib(self):
        if self.at("op", "<"):
            self.pos += 3

    def assign_name(self, name: str, val) -> None:
        s = self.scope.find(name)
        if s is None or s is self.r.globals:
            if name in self.r.frozen:
                return
            s = self.r.globals
        s.vars[name] = val

    def lookup(self, name: str):
        s = self.scope.find(name)
        if s is not None:
            return s.vars[name]
        return Ref(name)

    def funcbody(self, name: str = "", self_param: bool = False) -> Func:
        self.take("op", "(")
        params = ["self"] if self_param else []
        vararg = False
        while not self.at("op", ")"):
            if self.at("op", "..."):
                vararg = True
                self.pos += 1
            else:
                params.append(self.take("name"))
            if self.at("op", ","):
                self.pos += 1
        self.pos += 1
        start = self.pos
        end = self.skip_block()
        self.pos = end + 1
        return Func(params, vararg, start, end, self.scope, self.c, name)

    # -- expressions --------------------------------------------------------

    def exprlist(self) -> list:
        out = [self.expr()]
        while self.at("op", ","):
            self.pos += 1
            out.append(self.expr())
        return out

    def expr(self, limit: int = 0):
        k, v = self.peek()
        if (k == "kw" and v == "not") or (k == "op" and v in ("-", "#", "~")):
            self.pos += 1
            a = self.expr(_UNARY)
            if v == "not":
                left = not truthy(a)
            elif v == "-":
                n = number(a)
                left = -n if n is not None else None
            elif v == "#":
                left = len(a) if isinstance(a, str) else (len(a.array()) if isinstance(a, LuaTable) else None)
            else:
                left = None
        else:
            left = self.simple()
        while True:
            k, op = self.peek()
            if k not in ("op", "kw") or op not in _BINARY:
                return left
            prec = _BINARY[op]
            if prec <= limit:
                return left
            self.pos += 1
            right = self.expr(_RIGHT.get(op, prec))
            left = _binop(op, left, right)

    def simple(self):
        k, v = self.peek()
        if k == "num":
            self.pos += 1
            return v
        if k == "str":
            self.pos += 1
            return v
        if k == "kw":
            if v == "nil":
                self.pos += 1
                return None
            if v in ("true", "false"):
                self.pos += 1
                return v == "true"
            if v == "function":
                self.pos += 1
                return self.funcbody()
        if k == "op" and v == "...":
            self.pos += 1
            return self.scope.varargs[0] if self.scope.varargs else None
        if k == "op" and v == "{":
            return self.table()
        return self.suffixed()

    def table(self) -> LuaTable:
        self.take("op", "{")
        t = LuaTable()
        n = 1
        while not self.at("op", "}"):
            if self.at("eof"):
                raise _ParseError("unclosed table")
            if self.at("op", "["):
                self.pos += 1
                key = self.expr()
                self.take("op", "]")
                self.take("op", "=")
                t.set(key, self.expr())
            elif self.at("name") and self.at("op", "=", 1):
                key = self.take("name")
                self.pos += 1
                t.set(key, self.expr())
            elif self.at("op", "..."):
                self.pos += 1
                for x in self.scope.varargs:
                    t.set(n, x)
                    n += 1
            else:
                val = self.expr()
                t.set(n, val)
                n += 1
            if self.at("op", ",") or self.at("op", ";"):
                self.pos += 1
            elif not self.at("op", "}"):
                raise _ParseError("bad table field")
        self.pos += 1
        return t

    def args(self) -> list:
        k, v = self.peek()
        if k == "str":
            self.pos += 1
            return [v]
        if k == "op" and v == "{":
            return [self.table()]
        self.take("op", "(")
        if self.at("op", ")"):
            self.pos += 1
            return []
        vals = [self.expr()]
        while self.at("op", ","):
            self.pos += 1
            vals.append(self.expr())
        self.take("op", ")")
        return vals

    def suffixed(self, lvalue: bool = False):
        k, v = self.peek()
        if k == "name":
            self.pos += 1
            name = v
            val = self.lookup(v)
            target = ("name", v)
        elif k == "op" and v == "(":
            self.pos += 1
            val = self.expr()
            self.take("op", ")")
            name = None
            target = None
        else:
            raise _ParseError(f"unexpected {v!r}")
        while True:
            k, v = self.peek()
            if k == "op" and v in (".", "["):
                self.pos += 1
                if v == ".":
                    key = self.take("name")
                else:
                    key = self.expr()
                    self.take("op", "]")
                target = ("index", val, key)
                val = _index(val, key)
                name = None
            elif k == "op" and v == ":":
                self.pos += 1
                m = self.take("name")
                f = _index(val, m)
                val = self.invoke(f, m, [val] + self.args())
                target = None
            elif (k == "op" and v in ("(", "{")) or k == "str":
                label = name or (target[2] if target and target[0] == "index" and isinstance(target[2], str) else None)
                if label is None and isinstance(val, Ref):
                    label = val.path.rsplit(".", 1)[-1]
                val = self.invoke(val, label, self.args())
                target = None
                name = None
            else:
                break
        if lvalue:
            return target
        return val

    def invoke(self, f, label: str | None, args: list):
        hook = self.r.hooks.get(label) if label else None
        if hook is not None and not isinstance(f, Func):
            return hook(args)
        if isinstance(f, Func) or callable(f):
            return self.r.call(f, args)
        if hook is not None:
            return hook(args)
        if label and _COPY.search(label):  # a copy helper of the engine's
            return _copy_call(args)
        return None


#: Loops run at most this many times; longer ones are cut.
MAX_LOOP = 512


def _iterations(numeric: bool, over) -> list | None:
    """The values a `for` loop binds, when the reader knows them: a numeric range, or ipairs/pairs of a table."""
    if over is None:
        return None
    if numeric:
        nums = [number(x) for x in over[:3]]
        if len(nums) < 2 or any(x is None for x in nums):
            return None
        a, b = nums[0], nums[1]
        step = nums[2] if len(nums) > 2 else 1
        if not step:
            return None
        out = []
        x = a
        while (x <= b if step > 0 else x >= b) and len(out) < MAX_LOOP:
            out.append((x,))
            x += step
        return out
    fn, t = over
    if not isinstance(t, LuaTable):
        return None
    if fn == "ipairs":
        return [(i, v) for i, v in enumerate(t.array()[:MAX_LOOP], 1)]
    return [(k, t.get(k)) for k in t.keys()[:MAX_LOOP]]


def _index(val, key):
    if isinstance(val, LuaTable):
        return val.get(key)
    if isinstance(val, Ref):
        if isinstance(key, str):
            return Ref(f"{val.path}.{key}")
        if isinstance(key, (int, float)):
            return Ref(f"{val.path}[{key}]")
        return None
    return None


def _binop(op, a, b):
    if op == "and":
        return b if truthy(a) else a
    if op == "or":
        return a if truthy(a) else b
    if op == "..":
        if isinstance(a, (str, int, float)) and isinstance(b, (str, int, float)) \
                and not isinstance(a, bool) and not isinstance(b, bool):
            return _str(a) + _str(b)
        return None
    if op in ("==", "~="):
        if isinstance(a, Ref) or isinstance(b, Ref):
            return None
        eq = a == b if not isinstance(a, LuaTable) else a is b
        return eq if op == "==" else not eq
    x, y = number(a), number(b)
    if x is None or y is None:
        return None
    try:
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y if y else None
        if op == "//":
            return x // y if y else None
        if op == "%":
            return x % y if y else None
        if op == "^":
            return float(x) ** float(y)
        if op == "<":
            return x < y
        if op == ">":
            return x > y
        if op == "<=":
            return x <= y
        if op == ">=":
            return x >= y
        if op in ("&", "|", "~", "<<", ">>"):
            i, j = int(x), int(y)
            return {"&": i & j, "|": i | j, "~": i ^ j, "<<": i << j if 0 <= j < 64 else 0,
                    ">>": i >> j if 0 <= j < 64 else 0}[op]
    except (OverflowError, ValueError, ZeroDivisionError):
        return None
    return None


def _str(x) -> str:
    if isinstance(x, float) and x.is_integer():
        return f"{x:.1f}"
    return str(x)
