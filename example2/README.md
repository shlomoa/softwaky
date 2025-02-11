# SoftWaky

## Example 2

- Django app with angular material

### python

Python is assumed to be installed
- minimal version 3.11.1

#### virtual environment

##### Windows

```sh
python.exe -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Password: Example1

##### linux

### Django

#### Windows

Follow detailed instructions from [https://www.django-rest-framework.org/tutorial/quickstart/]

```sh
cd dj
django-admin startproject myproject .
cd myproject
django-admin startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```
 test run: python.exe .\manage.py runserver

### Angular

- node.js and npm are assumed to be installed

in vscode terminal:
```pwsh
ng new myproject --create-application false --style scss --skip-git true --routing true --directory ng --new-project-root myproject --defaults true --prefix myproject
ng generate application quickstart --prefix quickstart --routing true --style scss  --ssr false
```

- [Angular](https://angular.dev/tutorials/learn-angular)
    - [Material](https://material.angular.io/guide/getting-started)


### integration

#### Directory structure
- ng
    - projects
        - tutorial
- dj
    - myproject
        - tutorial

#### vscode

##### tasks
