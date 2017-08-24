## Overview
Django + Django Rest Framework project touching on multiple concepts in django web programming.
Some decisions are made as MVP steps, and should be extended; such as using a production database
instead of sqlite.

## Install steps.
Project is build using python 3.5 but should work for any version of python 3.

1) git clone https://github.com/ChrisBronkhorst/crunchy.git
2) cd crunchy
3) virtualenv env
4) source activate env
5) pip install -r requirements.txt
6) python manage.py migrate
7) python manage.py runserver


## Enviroment variables that need to be set
- secret_key