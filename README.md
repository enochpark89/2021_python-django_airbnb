# Airbnb Clone

-  This is to copy similar functional website as Airbnb with Django and Tailwind CSS etc.

# Programming languages/framework used

-  JS, HTML, CSS, Python, Django

# Software Requirement

-  [x] Python 3.0
-  [] Django
-  [x] pipenv

_Please look at the documentation on how to install these on your particular OS system._

# Progress journal

-  If you are serious about the career as a Django developer, we recommend using Pycharm community or professional version.
-  **Jetbrains**: The company who developed Pycharm. They have IDE for many programming languages.
-  Django vs Flask:
   -  Python: mininalistic (Flask, Pyramid), simple code; lots of manual work; invent wheels
   -  Django: massive framework; comes with many utilities; Use other ppl's work; no need to reinvent wheels.
-  If you use Django template, you will save alot of time building a website.
-  A web app that requires many user interactions should use React.
-  Sometimes, you do not need React to build a website. It might be better in some cases to use Django.
-  Pip installs everything globally. So we install something like **pipenv** that install packages within your environment only. The problem with installing globally is that when there is a version update, your code might break. Therefore, it is better for you to create a bubble or a backup just incase the code breaks.
-  Tell pipenv to create an environment with Python 3 (_pipenv --three_)

## 1.0 Create Env and Install Django

1. Create a working environment directory.
2. Create a python 3 environment - _pipenv --three_ > pipfile gets created; virtual environment is created.
3. In a terminal, run _pipenv shell_ gets a developer inside a virtual environment.
4. Install Django - _pipenv install Django==2.2.5_
5. To confirm Django installation, run _django-admin_ > If successfully installed, you get [django] with many options available.

## 1.1 Create a Github Repository.

## 1.2 Test the Bubble

-  Make sure to run pipen shell so that you will be in the bubble to work on the project.
-  Please make sure to run _pipenv shell_ if you turned off the computer or VSCODE.

## 1.3 Test the Bubble

-  Though the tutorial is telling people to use django-admin startproject, there is a better way to form an application.
-  Run _django-admin startproject config_
-  We have two folders (config, manage.py) > Take it ouside the config folder and delete the config folder that holds two files (config and manage.py).
-  Linter: looks at your code and tries to foresee the errors that might come up in the future.
   -  Flask 8 and pylint
-  Formatter
   -  Black: install Black - recommend which codes to format.
-  PEP8: A style guide that is recommended for a clean code. DOS AND DON'T (_Please read the documentation_)

## 1.4 First look at Django

-  **init** everytime you make a file you need to have **init.py**.
-  settings.py: everything is set up in the beginning to make the application that Django gives us. such as admin, auth, contenttypes, sessions, messages, static files, and middlewares, WSGI, DB.
-  Django comes with files and comments. These comments are very valuable because it explains about the pre-setting that is created.
-  Django documentation: Django documentations are available to all in the setting file. It shows the source, many of the things are done for us such as common password check and everything. look for things that you don't understand. Then, you just need to click on it. IF you have a question on anything, you can just click to see the detailed documentation.

-  **Manage.py**: have many commands. If you hover your mouse on, click command or control and you can enter into the related file.

-  Run _python manage.py runserver_ to start the server. The default localhost is 8000. (http://localhost:8000/)

   -  If you save any of the files, it will update the changed information.
   -  "/admin" shows an administrator page. It requires a login.

-  Run _python manage.py migrate_ > Then, run the server.
-  The Django administration will show. If you DO NOT have the user account, it is not going to allow access.

_Always check whether you are running the server_

-  To create a super user, you run _python manage.py createsuperuser_
-  You can create an admin account in like 2 seconds, and work on the administrative things. Everything is ready for you.

## 1.5 Django Migrations

-  Once you delete the Sql Lite and redo the migration, you will get many errors.
-  migration > creates db.sqlite3
-  DB is there but it is not synchronizing with Django.
-  SQL database is the most popular DB ever.
-  _PostgreSQL_ and _MySQL_ they are less professional with not advanced features. They both have rows and columns.
-  On the basic level, you are basically describing what data is going to be saved.
-  If we try to save the data, it will understand because we already stated what kinds of data will be saved.
-  Any OS, we have to describe some people do this by learning SQL to send this instruction directly to the DB.
-  Django comes with migration function. This in DB it is changing the shape of the DB from one to the other.
-  _For example, if we run python manage.py makemigrations_, it will look for models.
-  Therefore, because of this function in Django, you don't need to learn SQL.
- Django already applied 17 migrations after running *python manage.py migration*

