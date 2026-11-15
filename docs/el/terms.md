---
title: Όροι και άδεια
nav_order: 8
lang: el
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Όροι και άδεια {#terms-and-licence}

## Οι όροι της Eagle Dynamics {#eagle-dynamics-terms}

Διαβάστηκαν στις 2026-11-07 από το `Doc/license_en.txt` της εγκατάστασης (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Το αδειοδοτημένο «Program» περιλαμβάνει
«THE DATA SUPPLIED WITH IT». Ρήτρα 3.1:

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

Η ρήτρα 3.1 (a) απαγορεύει να «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» χωρίς συναίνεση, και η (e) να «exploit this
Program or any of its parts commercially».

Τι κάνει αυτός ο αναγνώστης: διαβάζει αρχεία δεδομένων στον δικό σας υπολογιστή, αφού τα έχετε εγκαταστήσει,
έξω από το παιχνίδι. Δεν αλλάζει τίποτα στο παιχνίδι, δεν σπάει καμία κρυπτογράφηση (το ένα κρυπτογραφημένο αρχείο
σε φάκελο εδάφους μένει ανέγγιχτο) και δεν μιλάει με κανέναν server. Η κατανόηση της διάταξης ενός αρχείου δεδομένων
είναι αντίστροφη μηχανική με την έννοια της ρήτρας 3.1 (c), και ένα επίπεδο χτισμένο από το έδαφος του παιχνιδιού
είναι ίσως παράγωγο έργο. Η χρήση του αναγνώστη είναι δική σας απόφαση, για δική σας χρήση· τα επίπεδα που γράφει
είναι δικά σας για προβολή, όχι για κοινοποίηση ή δημοσίευση. Γι' αυτόν τον λόγο είναι ξεχωριστό πακέτο.

Η επισήμως προβλεπόμενη εναλλακτική, που δεν διαβάζει κανένα αρχείο: το ίδιο το scripting των αποστολών του simulator
μπορεί, όσο τρέχει μια αποστολή, να δειγματίσει το έδαφος (`land.getHeight`, `land.getSurfaceType`) και να
απαριθμήσει τα αεροδρόμια (`world.getAirbases`). Χρειάζεται το DCS να τρέχει για ώρες ανά θέατρο και δίνει
πιο αραιό πλέγμα· δεν υλοποιήθηκε, επειδή τα αρχεία αποδείχθηκαν αναγνώσιμα.

## Άδεια και πηγές {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Χρειάζεται το numpy (BSD-3-Clause)· το `fit` σε
`.parquet` χρειάζεται το pyarrow (Apache-2.0). Γράφτηκε για αυτό το έργο. Οι σταθερές της προβολής είναι στοιχεία
που δημοσιεύει το pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`)· πάρθηκαν μόνο οι αριθμοί. Η προβολή είναι
οι σειρές του Krüger όπως τις δίνει ο C. F. F. Karney («Transverse
Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). Δεν πάρθηκε κώδικας από κανένα άλλο έργο.
