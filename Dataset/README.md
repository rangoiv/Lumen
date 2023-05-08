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

Učitavanje oznaka (eng. label) ovisi o folderu. 
U IRMAS_Training_Data ih učitava preko regexa - prva oznaka unutar uglatih zagrada. 
Sve ostale učitava kao u IRMAS_Validation_Data - iz tekstualne datoteke.

### BITNO!

Kako su datoteke odsijecane abecedno (kao opisano u projektnoj dokumentaciji), ovdje će se nalaziti prva datoteka IRMAS_Validation_Data kao što se i nama nalazi. To je dovoljno da se iz IRMAS dataseta može potpuno imitirati naš postupak i naš dataset (samo se pomakne sve od te datoteke nadalje u novi folder).