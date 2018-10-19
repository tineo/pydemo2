# Django for Heroku

An utterly fantastic project starter template for Django 1.11.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment (or 3.5 in Ubuntu :v). 

## How to Use

To use this project, follow these steps:

1. Create your working environment. [How i do it :)](https://gist.github.com/tineo/7423f2916108d964a2a65d0f9a3e9472)
2. Install Django (`$ pip3 install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/tineo/pydalgom/archive/master.zip --name=Procfile newproject

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``newproject`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate
## But you should use github
    $ git init
    $ git add .
    $ git commit -am "Initial d"
    $ git remote add origin https://github.com/your_username/your_project.git
    
    Then push Deploy Button on Heroku panel ;D
    
See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7? (Nah, I prefer to use py3)

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
