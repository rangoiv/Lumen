# REST API FOR LUMEN APP

_PyTissue_: Goran Ivanković, Luka Ivanković

## How to setup

In ../environments directory there are 2 environents. This code should work on both environments.

do:

`$ conda env create -f environment.yml`

check if it is correctly installed:

`$ conda env list`

Activate the environment:

`$ conda activate pytissue`

### Virtual env not working?

(if you have correctly set up virtual environment, you can skip this step)
Before running, you need to satisfy dependencies, commands should be run in following order:

pip install django
pip install django-cors-headers
pip install librosa
pip install torch
pip install fastai

Also, install:

pip install nbformat
pip install nbconvert

## Run app

After that, you should run manage.py like this:

`$ python manage.py runserver`

Make sure all dependencies are satisfied before running command above.
Install any dependency that is missing in your python environment.

Aditional help with installing above dependencies:

https://docs.fast.ai/
https://pytorch.org/get-started/locally/
https://docs.djangoproject.com/en/1.8/howto/windows/
https://bobbyhadz.com/blog/python-no-module-named-corsheaders