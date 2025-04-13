## Most common commands in Django

### Start a project in Django in the actual directory
```
django-admin startproject my_project_name .
```
### Run a server
```
python manage.py runserver port_number
```
### Commands help
```
python manage.py --help
```
### Create app inside project
```
python manage.py startapp my_app_name
```
### Search and create file for migrations
```
python manage.py makemigrations (optional: app_name)
```
### Run migrations
```
python manage.py migrate (optional: app_name)
```
### Django shell 
```
python manage.py shell
```
### Create superuser admin
```
python manage.py createsuperuser
```
### List all dependencies
```
pip freeze > requirements.txt
```
### Check all fields in a record in the shell (example)
```
Product.objects.first().__dict__
```
