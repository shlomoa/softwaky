# SoftWaky

## Example 1

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
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```
 test run: python.exe .\manage.py runserver

### Angular

- node.js and npm are assumed to be installed

in vscode terminal:
```pwsh
ng new myproject --create-application false --style scss --skip-git true --routing true --directory ngenv --new-project-root myproject
```

- [Angular](https://angular.dev/tutorials/learn-angular)
    - [Material](https://material.angular.io/guide/getting-started)

#### building
- for integration:
    - ng build --prod --output-path ..\beci\app\static\angular --output-hashing none --watch
- for testing frontend 
    - ng build --output-hashing none --watch

### integration


#### vscode

##### tasks
