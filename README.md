# SoftWaky

## Example 1

- Django app with angular material

- technologies
[Python][def]  [Django][def]  [Angular][def]

### Build 

- angular in vscode on Windows
    - for integration:
        ```pwsh
        cd ng
        ng build --prod --output-path ..\beci\app\static\angular --output-hashing none --watch
        ```
    - for testing frontend only:
        ```pwsh
        cd ng
        ng build --output-hashing none --watch
        ```
- Django in vscode on windows
    - for integration with ng
        ```pwsh
        cd dj
        python manage.py collectstatic
        ```
    - for testing backend only
        ```pwsh
        cd dj
        python manage.py makemigrations
        python manage.py migrate
        python manage.py collectstatic
        ```

### test

- Angular frontend only in vscode on Windows
    ```pwsh
    cd ng
    ng serve
    ```
- Django backend only in vscode on Windows
    ```pwsh
    cd dj
    python.exe .\manage.py runserver
    ```

[def]: /shlomoa/docs/python.md
[def]: /shlomoa/docs/django.md
[def]: /shlomoa/docs/angular.md