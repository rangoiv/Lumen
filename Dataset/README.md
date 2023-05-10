# Dataset

## Opis

Mogući instrumenti i njihove oznake su: violončelo (cel), klarinet (cla), flauta (flu),
akustična gitara (gac), električna gitara (gel ), orgulje (org), klavir (pia), saksofon (sax),
truba (tru), violina (vio) i ljudski pjevački glas (voi).

Dodatno, neke od datoteka imaju bilješke u nazivu datoteke koje se odnose na prisut-
nost ([dru]) ili nepostojanje ([nod]) bubnjeva i glazbeni žanr: country-folk ([cou-fol]),
klasika ([cla]) , pop-rock ([pop-roc]), latino-soul ([lat-sou]).

## Struktura direktorija

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

## Postupak raspodjele

Kako su datoteke odsijecane abecedno (kao opisano u projektnoj dokumentaciji), ovdje će se nalaziti prva datoteka IRMAS_Validation_Data kao što se i nama nalazi. To je dovoljno da se iz IRMAS dataseta može potpuno imitirati naš postupak i naš dataset (samo se pomakne sve od te datoteke nadalje u novi folder).

Preciznije, pratiti sljedeće korake:

1) Iz originalnog IRMAS_Validation_Data kopirati sve pjesme (i .txt oznake) do uključivo `01. Offering-11.wav` u naš folder IRMAS_Validation_Data. Trebalo bi ih sada biti ukupno 1272, uključujući tekstualne datoteke.

2) Ostatak IRMAS_Validation_Data, dakle počevši od datoteke `01. Offering-12.txt`, kopirati u naš IRMAS_Test_Data. U IRMAS_Test_Data bi se sada trebalo nalaziti 4476 datoteka.

3) Kopirati cijeli IRMAS_Training_Data u naš IRMAS_Training_Data, bez izmjena.

4) Kopirati svih 103 datoteka testnog dataseta u `test_dataset`.

Backend i bilježnica bi se trebale moći pokretati i bez toga, jer su neke datoteke već unutra, ali se neće vidjeti rezultati kakve smo mi dobivali.