# Preparing and creating a djangoroject


## Create project
```bash
mkdir django && cd django
virtualenv -p python3 .
source ./bin/active
```
```bash
pip3 install django
django-admin startproject projectname .
```

## create inital sqlite.db and add superuser
```bash
# creates db
python3 manage.py migrate

# creates superuser
python3 manage.py createsuperuser
```

## creating apps in your application
```bash
python3 manage.py startapp appname
```
