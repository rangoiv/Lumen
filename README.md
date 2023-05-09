# Prepoznavanje instrumenata - Lumen

_PyTissue_: Goran Ivanković, Luka Ivanković

## Zadatak

Program koji prepoznaje pojavljene instrumente u `.wav` datotekama od 11 mogućih instrumenata.

## Struktura direktorija

- **main.ipynb** -
Ovdje se nalazi kod za učitavanje neuronske mreže, njezino treniranje te sve augmentacije.
Također sadrži funkciju koja kreira konačni json za test dataset (na kraju) bilježnice.

- **lumenback** -
Direktorij za Django API. Pri pokretanju učitava pomoćne funkcije (za klizeće prozore i
slično) iz bilježnice main.ipynb. Osim toga učita najbolji model koji imamo iz foldera
models. Pomoću toga detektira instrumente u poslanim datotekama.
Upute za pokretanje nalaze se u tom direktoriju.

- **lumenfront** -
Direktorij za React frontend aplikaciju. Aplikacija ima sučelje za snimanje zvuka (koje nije do kraja uspjelo proraditi) i za slanje datoteka. U pozadini poziva backend API za detekciju instrumenata. Stoga je potrebno prvo pokrenuti lumenback, da bi lumenfront radio.

- **notebooks** - 
Dodatne bilježnice za analizu dataseta

- **models** -
Spremljene težine modela. Trebao bi biti spremljen samo `MLBLCLA2_model.pth` koji daje najbolje rezultate. **Bitno**: te težine *ne* nalaze se u github repozitoriju, ali će biti predane u rješenju. Program bez njih ne može učitati model i neće raditi.

- **environments** - 
Svi conda environmenti koji su potrebni. Dodatne upute se nalaze u *Kako pokrenuti*.

- **Dataset** - 
Tu se nalazi IRMAS dataset kao opisan u našoj dokumentaciji. Dodatne upute nalaze se unutra u `README` datoteci.

- **preds.json** - Predviđanja modela za testni dataset.


## Kako učitati conda okruženje?

Za backend i bilježnicu imamo dvije opcije:

1) Bez GPU
1) Sa GPU

Za obje opcije spremili smo conda okruženja u  environments folder.
Prednost korištenja GPU je puno brže izvršavanje.
U folderu environments nalaze se sljedeća dva okruženja:

- fastai-gpu.yml: okruženje za wsl za GPU
- environment.yml: obično okruženje

Pokrenuti `conda env create -f <environment.yml>`. Pritom zamijeniti `<environment.yml>` sa odgovarajućim okruženjem.

Nakon učitavanja okruženja, pratiti upute za pokretanje.

### Napomene za GPU

- Potrebno je imati Nvidia GPU (jer se koristi Cuda). 
- Koristili smo wsl za i mambu za kreiranje okruženja.
- Dodatne upute nalaze se u `GPU_SETUP.md`. 

Ukratko, na `wsl` smo preuzeli **cudu** (program za korištenje Nvidia GPU) i **mambu** (brža verzija conde) te onda preuzeli potrebne Python biblioteke. Trebalo bi raditi i sa običnom condom, ali nismo provjerili. Sumnjamo da će raditi bez wsl-a, ali vrijedi pokušati.

## Kako pokrenuti?

Kako pokrenuti React frontend nalazi se u lumenfront `README` datoteci. 

Kako pokrenuti Django backend nalazi se u lumenback `README` datoteci.

Za pokretanje bilježnice, aktivirati odgovarajuće okruženje:

`conda activate fastai` ili `conda activate pytissue`.

Upisati `jupyter notebook` te otvoriti `main.ipynb` u pregledniku.


