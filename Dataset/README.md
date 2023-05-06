# Dataset

_PyTissue_: Goran Ivanković, Luka Ivanković


U ovom direktoriju nalazi se po jedna datoteka za svaki folder (kako bi se folder pojavio na githubu), tako da korištena struktura direktorija bude jasna.

- Dataset
    - IRMAS_Training_Data
        - cel
        - cla
        - flu
        - ...
    - IRMAS_Validation_Data (prvih 20% originalnog IRMAS_Validation_Data, koristi se kao dio train seta)
    - IRMAS_Test_Data (preostalih 80% originalnog IRMAS_Validation_Data, koristi se kao validation set)
    - test_dataset (dataset koji je poslan kao zadatak)

Bitno je da je IRMAS_Training_Data folder postavljen kao ovdje (zajedno sa datotekama) jer ih fastai učitava prilikom kreiranja dataloadera i modela. Pomoću svih dostupnih datoteka napravit će konačni vocabulary (cel, cla, flu ... - ukupno 11 instrumenata). Ako nema barem jedne datoteke od svih instrumenata, neće izgraditi cijeli vocabulary. Stoga neće moći ni učitati težine našeg modela, jer ima drugačiju građu (drugačiji output layer).

Učitavanje oznaka (eng. label) ovisi o folderu. Zato je također bitno da se datoteke ne miješaju, već se postave točno kako smo ih mi postavili.

### BITNO!

Kako su datoteke odsijecane abecedno (kao opisano u projektnoj dokumentaciji), ovdje će se nalaziti prva datoteka IRMAS_Validation_Data kao što se i nama nalazi. To je dovoljno da se iz IRMAS dataseta može potpuno imitirati naš postupak i naš dataset (samo se pomakne sve od te datoteke nadalje u novi folder).