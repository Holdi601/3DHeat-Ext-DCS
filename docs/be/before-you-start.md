---
title: "Перад пачаткам"
nav_order: 1.5
lang: be
source: before-you-start.md
source_hash: "64346abe88e5"
nav_exclude: true
search_exclude: true
---
# Перад пачаткам {#before-you-start}

Упершыню ў камандным радку? Гэтая старонка правядзе вас ад нуля да першага
запуску. Гэта займае каля дзесяці хвілін, і толькі адзін раз.

## 1. Усталюйце Python {#install-python}

Для гэтага інструмента патрэбны **Python 3.10 або навейшы**.

- **Windows:** спампуйце Python з [python.org/downloads](https://www.python.org/downloads/)
  і запусціце ўсталёўшчык. На першым экране адзначце **Add python.exe to PATH**,
  потым націсніце **Install Now**.
- **macOS і Linux:** Python 3 часта ўжо ёсць. Дзе на гэтых старонках напісана
  `python`, друкуйце `python3`.

## 2. Атрымайце гэты інструмент {#get-this-tool}

Адкрыйце [github.com/Holdi601/3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS), націсніце зялёную
кнопку **Code**, потым **Download ZIP** і распакуйце архіў у любую
папку. Калі вы карыстаецеся git: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`.

## 3. Адкрыйце тэрмінал у гэтай папцы {#open-a-terminal-in-that-folder}

Тэрмінал — гэта акно, у якім друкуюць каманды.

- **Windows:** адкрыйце папку ў Правадыру, пстрыкніце ў адрасным радку, увядзіце
  `powershell` і націсніце Enter. Адкрыецца сіняе або чорнае акно, ужо ў гэтай
  папцы.
- **macOS:** адкрыйце **Terminal**, увядзіце `cd ` (з прабелам), перацягніце папку ў
  акно і націсніце Enter.

`cd` значыць «змяніць папку»: `cd C:\Tools\3DHeat-Ext-DCS` пераходзіць у гэтую папку.

## 4. Усталюйце інструмент {#install-the-tool}

Увядзіце гэта і націсніце Enter:

```bash
python -m pip install -e .
```

У канцы вы ўбачыце: `Successfully installed heat3d-ext-dcs-...`.

## 5. Запусціце яго {#run-it}

```bash
heat3d-dcs-maps list
```

Вы ўбачыце нешта накшталт:

```text
DCS World at C:\Games\DCS World
  <theatre>    <n> GB    <n> tiles    <n> M vertices  lat/lon    readable
```

Далей: [Пошук тэатраў: list](list.md), потым [Пабудова ўзроўню: level](level.md).

## Як чытаць каманды на гэтых старонках {#how-to-read-the-commands-on-these-pages}

| Вы бачыце | Што гэта значыць |
|---|---|
| `<folder>` | запаўняльнік: увядзіце сваё значэнне замест яго, без `< >` |
| `[--force]` | неабавязкова: прапусціце або ўвядзіце, як паказана |
| `a\|b` | выбар: увядзіце `a` або `b` |
| `# a note` | каментар для вас: не друкуйце яго |
| `"C:\My Files\x"` | шлях з прабеламі бярыце ў двукоссі |
| `D:\Demos` | прыклад папкі ў Windows: бярыце сваю |

## Калі нешта пайшло не так {#when-something-goes-wrong}

| Паведамленне | Што рабіць |
|---|---|
| `'python' is not recognized` | Python не ўсталяваны, або не адзначылі PATH: усталюйце яго зноў і адзначце (або друкуйце `py` замест `python`). |
| `'heat3d-dcs-maps' is not recognized` | Паўтарыце крок 4 у папцы інструмента, або друкуйце `python -m heat3d_ext_dcs` замест `heat3d-dcs-maps`: гэта тое самае. |
| `No module named heat3d_ext_dcs` | Вы не ў папцы інструмента, або крок 4 не ўдаўся: перайдзіце туды праз `cd` і выканайце крок 4. |
| `No module named pip` | Выканайце `python -m ensurepip`, потым крок 4. |
| што заўгодна іншае | Прачытайце апошні радок паведамлення, потым адкрыйце issue на GitHub з ім. |

Кожная каманда таксама заканчваецца **кодам выхаду**: 0 значыць, што ўсё атрымалася. Каб убачыць яго,
увядзіце `echo $LASTEXITCODE` у PowerShell або `echo $?` на macOS і Linux.
