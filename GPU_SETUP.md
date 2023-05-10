# Prepoznavanje instrumenata - Lumen

## How to setup fastai using GPU

For this tutorial to work fine, you need to have Nvidia GPU and windows. For
Linux and additional info, go [here](https://anaconda.org/fastai/fastai) or
watch [this video](https://youtu.be/F4tvM4Vb3A0?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU&t=3265).

If you are running windows, first install wsl (Windows subsystem for Linux). You can run it
by opening command prompt and running `> wsl`.

To make sure everything is up-to-date run:

`$ sudo apt update && sudo apt upgrade --yes`

After this, you will install mamba (similar to conda) and all the required libraries to run 
the app in wsl.
Also, each time you run the app, you will also need to first start up wsl. 

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

#### Other libraries

To run backend API, you will need django and some other libraries.

`$ mamba install -c conda-forge django`

`$ mamba install -c conda-forge django-cors-headers`

To see how to run backend API, check out README.md inside the lumenback
folder.

## Run Jupyter notebook

Open wsl and activate fastai environment.

Place yourself in folder where you installed this Lumen repo, for example
I would run `cd /mnt/c/Users/Rango/Projects/Lumen/`. In wsl you can access
other drives with `/mnt/drive_letter`. Then run jupyter notebook from there:

`$ jupyter notebook --no-browser`

Open one of the URL-s printed in terminal.
