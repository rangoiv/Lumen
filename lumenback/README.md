# REST API FOR LUMEN APP

_PyTissue_: Goran Ivanković, Luka Ivanković

## How to setup

List of dependencies is in requirements.txt.
You can create virtual environment with above dependencies, instructions:
https://stackoverflow.com/questions/14684968/how-to-export-virtualenv

Create "models" folder: "lumenback/models"
put MLBLCLA_model.pth inside that folder.

After that navigate to this directory "lumenback" and run following:

`$ python manage.py runserver`

Make sure all dependencies are satisfied before running command above.

### Not working?

If setuping virtual environment didn't work, you can run following commands in this order:

pip install django
pip install django-cors-headers
pip install torch
pip install fastai
pip install librosa

Or install any dependency that is missing in your python environment.

Aditional help with installing above dependencies:

https://docs.fast.ai/
https://pytorch.org/get-started/locally/
https://docs.djangoproject.com/en/1.8/howto/windows/
https://bobbyhadz.com/blog/python-no-module-named-corsheaders