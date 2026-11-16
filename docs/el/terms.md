---
title: Όροι και άδεια
nav_order: 8
lang: "el"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Όροι και άδεια {#terms-and-licence}

## Τι διαβάζει ο αναγνώστης {#what-the-reader-reads}

Ο αναγνώστης διαβάζει αρχεία δεδομένων της δικής σας εγκατάστασης του DCS World στον υπολογιστή σας ([Πώς διαβάζονται τα αρχεία](reading.md)). Δεν αλλάζει τίποτα στο παιχνίδι και δεν επικοινωνεί με κανέναν διακομιστή.

Τίποτα από το παιχνίδι δεν συνοδεύει το εργαλείο ούτε αναδιανέμεται: κανένα αρχείο του παιχνιδιού, κανένας κώδικας του παιχνιδιού, κανένα DLL· τα τεστ φτιάχνουν μόνα τους κάθε αρχείο που διαβάζουν. Τα επίπεδα που γράφει μένουν στον υπολογιστή σας.

Το 3DHeat DCS δεν συνδέεται με την Eagle Dynamics ούτε έχει την έγκρισή της. Το DCS World και τα σχετικά ονόματα και εμπορικά σήματα ανήκουν στους κατόχους τους.

Δικαιούχοι: ανοίξτε ένα θέμα στο [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - απαντάμε γρήγορα και αφαιρούμε οτιδήποτε κατόπιν αιτήματος.

## Άδεια και πηγές {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Χρειάζεται το numpy (BSD-3-Clause)· το `fit` σε
`.parquet` χρειάζεται το pyarrow (Apache-2.0). Γράφτηκε για αυτό το έργο. Οι σταθερές της προβολής είναι στοιχεία
που δημοσιεύει το pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`)· πάρθηκαν μόνο οι αριθμοί. Η προβολή είναι
οι σειρές του Krüger όπως τις δίνει ο C. F. F. Karney («Transverse
Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). Δεν πάρθηκε κώδικας από κανένα άλλο έργο.
