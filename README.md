# Prepoznavanje instrumenata - Lumen

_PyTissue_: Goran Ivanković, Luka Ivanković


## Zadatak
Mogući instrumenti i njihove oznake su: violončelo (cel), klarinet (cla), flauta (flu),
akustična gitara (gac), električna gitara (gel ), orgulje (org), klavir (pia), saksofon (sax),
truba (tru), violina (vio) i ljudski pjevački glas (voi).

Dodatno, neke od datoteka imaju bilješke u nazivu datoteke koje se odnose na prisut-
nost ([dru]) ili nepostojanje ([nod]) bubnjeva i glazbeni žanr: country-folk ([cou-fol]),
klasika ([cla]) , pop-rock ([pop-roc]), latino-soul ([lat-sou]).

## How to setup fastai

For this tutorial to work fine, you need to have Nvidia GPU and windows. For
Linux and additional info, go [here](https://anaconda.org/fastai/fastai) or
watch [this video](https://youtu.be/F4tvM4Vb3A0?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU&t=3265).

If you are running windows, first install wsl (Windows subsystem for Linux). You can run it
by opening command prompt and running `> wsl`.

To make sure everything is up-to-date run:

`$ sudo apt update && sudo apt upgrade --yes`

#### Install Mamba

Mamba is a tool to help you manage conda environments. The reason we are
using it instead of regular conda is that Mamba is much faster.

`$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"`

`$ bash Mambaforge-$(uname)-$(uname -m).sh`

Create your mamba environment for fastai with 

`$ mamba create fastai` 

And then 
activate it 

`$ mamba activate fastai`.


Full process can be found
[here](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html).

#### Install fastai

Type `cd` to go to home directory on your Linux. Git clone 
this [GitHub repository](https://github.com/fastai/fastsetup).

`$ git clone https://github.com/fastai/fastsetup.git`

`$ cd ./fastsetup`

`$ mamba install -c pytorch -c nvidia -c fastai anaconda`

To install Jupyter notebook, run:

`$ mamba install -c pytorch -c nvidia -c fastai nbdev`

`$ mamba install -c pytorch -c nvidia -c fastai notebook`

## Run Jupyter notebook

Place yourself in folder where you installed this Lumen repo, for example
I would run `cd /mnt/c/Users/Rango/Projects/Lumen/`. In wsl you can access
other drives with `/mnt/drive_letter`. Run jupyter notebook:

`$ jupyter notebook --no-browser`

Open one of the URL-s printed in terminal or open it with PyCharm and
inserting the link to _configure Jupyter server..._ setting.