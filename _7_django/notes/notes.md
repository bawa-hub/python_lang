# create virtual environment

python3 -m venv myvenv

# activate venv

source /path/to/myvenv/bin/activate

# install dependencies

pip3 install -r requirements.txt

# start django project

pip install django
django-admin startproject <projectname>

# make apps

cd project
python manage.py startapp <appname>

# start server

python manage.py runserver

# make and run migration

python manage.py makemigrations
python manage.py migrate

# run django shell

python manage.py shell

# django admin panel

python manage.py createsuperuser
