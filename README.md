# Prepoznavanje instrumenata - Lumen

_PyTissue_: Goran Ivanković, Luka Ivanković

## Zadatak

Program koji prepoznaje pojavljene instrumente u `.wav` datotekama od 11 mogućih instrumenata.

## Dataset

Mogući instrumenti i njihove oznake su: violončelo (cel), klarinet (cla), flauta (flu),
akustična gitara (gac), električna gitara (gel ), orgulje (org), klavir (pia), saksofon (sax),
truba (tru), violina (vio) i ljudski pjevački glas (voi).

Dodatno, neke od datoteka imaju bilješke u nazivu datoteke koje se odnose na prisut-
nost ([dru]) ili nepostojanje ([nod]) bubnjeva i glazbeni žanr: country-folk ([cou-fol]),
klasika ([cla]) , pop-rock ([pop-roc]), latino-soul ([lat-sou]).

## Struktura direktorija

- **main.ipynb** -
Ovdje se nalazi kod za učitavanje neuronske mreže, njezino treniranje te sve augmentacije.
Također sadrži funkciju koja kreira konačni json za test dataset (na kraju) bilježnice.

- **lumenback** -
Direktorij za Django API. Pri pokretanju učitava pomoće funkcije (za klizeće prozore i
slično) iz bilježnice main.ipynb. Osim toga učita najbolji model koji imamo iz foldera
models. Pomoću toga detektira instrumente u poslanim datotekama.
Upute za pokretanje nalaze se u tom direktoriju.

- **lumenfront** -
Direktorij za React frontend aplikaciju. Aplikacija ima sučelje za snimanje zvuka (koje nije do kraja uspjelo proraditi) i za slanje datoteka. U pozadini poziva backend API za detekciju instrumenata. Stoga je potrebno prvo pokrenuti lumenback, da bi lumenfront radio.

- **notebooks** - 
Dodatne bilježnice za analizu dataseta

- **models** -
Spremljene težine modela. Trebao bi biti spremljen samo `MLBLCLA2_model.pth` koji daje najbolje rezultate.

- **environments** - 
Svi conda environmenti koji su potrebni. Dodatne upute se nalaze u *Kako pokrenuti*.

- **Dataset** - 
Tu se nalazi IRMAS dataset kao opisan u našoj dokumentaciji. Dodatne upute nalaze se unutra u `README` datoteci.


## Kako pokrenuti?

Kako pokrenuti frontend nalazi se u lumenfront `README` datoteci

Za backend i bilježnicu imamo dvije opcije:

1) Bez GPU
1) Sa GPU

Za obje opcije spremili smo conda okruženja u  environments folder.
Prednost korištenja GPU je puno brže izvršavanje. 

### Kako učitati conda okruženje

Pokrenuti `conda env create -f <environment.yml> --name <name>`. Pritom zamijeniti `<environment.yml>` sa odgovarajućim okruženjem te `<name>` sa imenom.

### Napomene za GPU

- Potrebno je imati Nvidia GPU (jer se koristi Cuda). 
- Dodatne upute nalaze se u `GPU_SETUP.md`. 

Ukratko, koristili smo `wsl`, na njega preuzeli **cudu** i **mambu** (brža verzija conde) i onda preuzeli potrebne Python biblioteke. Trebalo bi raditi i sa običnom condom, ali nismo provjerili.

