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

# 1.0 Introduction to Django

## 1.1 Create Env and Install Django

1. Create a working environment directory.
2. Create a python 3 environment - _pipenv --three_ > pipfile gets created; virtual environment is created.
3. In a terminal, run _pipenv shell_ gets a developer inside a virtual environment.
4. Install Django - _pipenv install Django==2.2.5_
5. To confirm Django installation, run _django-admin_ > If successfully installed, you get [django] with many options available.

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
-  Django already applied 17 migrations after running _python manage.py migrate_

## 1.6 Django Application

-  Before you start, we need to think about how are we going to organize our application.
-  Project is a groups of apps. Apps are a group of functions.
-  When you visit AirBnB site, you see that there are multiple functions that you need to create.
-  The word room should be a group.
-  You notice that rooms also have reviews.
-  you can review a room so it is related.
   -  rooms folder: handling room search, room reservation
   -  user folder: login,
-  you should have one big application. You have to divide and conquer.
-  the functions should be simplified and divided.
-  Once you make a seperate applications, we can put all things together and import it in the configuration.
-  We need to know what application to create. The rule of thumb is that you should be able to describe an application with a simple term.

## 1.7 Create App

-  **django-admin startapp** will start an app.

Steps:

1. Create Applications: django-admin startapp rooms > The rooms folder gets created.

-  users
-  lists
-  reservations
-  reviews
-  conversations

2. Each folder is like its own application.
3. We need to create User's application for them to work on their own profile.
4. Applications come with file. The names of these files must stay what they are. You are using a framework, not a library. With a framwork, you play by the rules of a framwork. With React, you can do whatever you want. But for Django, you have to follow its rule.

-  For example, if you want to change the URL, Django will look for the change in certain files.
-  even all the variables in the settings are configured in certain ways for a reason. DO NOT TOUCH

5. Though the names in the application folders are not modifiable, you can create a new folder for your own sake. For example, we are going to create urls.py file to keep track of all URLS.

# 2.0 User App

# 2.1 Replace Default User

-  There is a concept called inheritance.
-  Django already comes with an user autentication and Admin panel.
-  The problem is that it is not big enough for us. We need to take the current capabilities and extend it because the page needs to be like an AirBnB website.
-  Django already has the user DB.
-  We can't change that on the fly. We need to change the Config/change.py
-  You can find this information in Django Docs > Search _Auth user_
-  Model is the way your data looks like.

Steps:

1. Go to users/Config/setting.py >
2. Go to _user/model.py_ > We are going to import the AbstractUser. It has many stuff for you already\_
3. Install a user application from the setting. Whatever you update from the setting.py, Django is going to update it.
   \*\*

## 2.2 User Model

_Error: Dependency on app with no migrations: users_

-  In order to get rid of this error, we need to create a migration.

Create Migration:

1. Run _python manage.py makemigrations_ to prepare for a migration.
2. Migration file gets updated w/o having to write any SQL.
3. Run _python manage.py migrate_
4. To confirm, run the server by _python manage.py runserver_
5. Server is created successfully!

Create a superuser:

1. Run _python manage.py createsuperuser_
2. Fill out the information.
3. You may now login with the ID and the passwords created.

-  We replaced the default admin with this project admin.

Design a model:

-  We know that the user already has bunch of variable in migration/0001*initial.py where it says \_fields=[]*

Steps:

1. In order to change the model of an admin panel, modify as below:
   admin.py:

```python
from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

```

2. Admin Panel addes a new row that manage users with default fields.
3. After this set up, you can write in the model. Model talks to Django > Django makes a form > Provide DB information and request for migration.

4. Create fields in the models.py. (_Please look at the documentation (There are many fields that Django offers)_)
   model.py:

```python
bio = models.TextField(default="")
```

5. Run migration _python manage.py makemigrations_. Otherwise, DB will not be aware of the changes made in model.py.
6. Run migrate _python manage.py migrate_
7. Restart the server
8. You will see in the user administration that the bio field has been created in the form that you indicated.

## 2.2 First Model Fields

-  It is a good practice to keep track of the new column or field in an excel sheet. New field "bio" is now created.
-  Every field requires a default value because there are going to be empty fields that might cause an error later on.
-  There are two ways to avoid an issue later:

1. Create a default
2. Allow null value.

-  Convention in the python is to create a comment whenever the class is created as below

```python
class User(AbstractUser):
    """Custom User Model"""
```

Populate more models:

1. Add more models as below:

```python
class User(AbstractUser):
    """Custom User Model"""
   avatar = models.ImageField()
   gender = models.CharField(max_length=10, null=True)
   bio = models.TextField(default="")
```

_We need pillow library to implement imageFiled. Please install it using pip_

2. Run _pipenv install Pillow_

3. **Make Migration & Migrate** (repeat above explanation)

4. We need to create a restiction on the fields with options. We can create choices as below:

```python
GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
```

-  Gender now has three options (Male, Female, and Other.)

## 2.3 Add more User Model

-  Update model.py to include more fields such as birthdate, language, currency, and superhost.
-  _Please refer to the model.py and comments_

## 2.4 Admin Panel

-  Django expects files within some folders to work with what you have. Therefore, we need to go by Django's rule.
-  There are two ways of making model show up in an admin panel

1. admin.site.register(<model>, <class>)
2. ModelAdmin.list_display.

-  You can add below code to add columns in your admin panel.

```python
    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
```

## 2.5 UserAdmin and CustomAdmin

-  _Fieldsets_: a group of many fields (blue thing)
-  Fieldsets is tuples.

admin.py

```python
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                )
            },
        ),
    )

    """
```

-  Now the blue fieldset is created for the admin user > Change User profile.
-  We lost Django fields because we registered fields in admin.py. In order to add Django fields back, just add UserAdmin.fieldsets.

```
# Combine user fieldsets with the
fieldsets = UserAdmin.fieldsets + (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                )
            },
        ),
    )
```

**Recap**:

1. Created Django Projects (folders)
2. There are many applications, group of functionalities.
   _Tip: Django uses the code and talks to the DB (Object relational method to communicate and to render)_
3. Models are made of fields. We updated many models. There are many pre-made filters that filter out wrong or bad data.
4. Admin panel modification is done on admin.py.
5. If you want to see your model in admin.py, you have to register it _EX: @admin.register(model.User), known as "decorator"._
6. When you create a class next to a decorator, the class controls the model specified in a decorator.
   OR you could have done admin.site.register() method
7. Django will look for keywords such as **fieldsets** to modify or render an admin panel.
8. If you put UserAdmin in the argument, you can use all default Admin panel fields and within the class.
9. For details, please take a look at model.py, admin.py, and migrations folder in users App.

# 3.0 Room App

## 3.1 Room Apps

Steps:

1. Install room apps in INSTALLED APPLICATION.
2. Add a model in rooms/models.py
3. If you create a variable in each app, this one has to be declared in every other .py file.
4. Therefore, create a core app that holds all the central variables. All the models will be extended from the core.

-  For example, TimeStampedModel will be copied an pasted in the core because this will be used in other models.

```py
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

   # Abrstact Model Meta that DOES NOT go to the db.
    class Meta:
        abstract = True
```

5. Whenever, new application is installed, please make sure to state it in the config/settings.py "PROJECT_APPS"
6. After setting up the TimeStamped Model, a developer can use it in other models by putting it as an argument of a class as below:

```python
class Room(core_models.TimeStampedModel):
```

7. Create fields for a Room app:
   -  name: req.
   -  description: req.
   -  country: req. (
      Use Django country library -
      a. Run _pipenv install Django-countries_
      b. Add django_countries to INSTALLED_APPS
      )
8. Use the Django countries by importing it.

_Tips: To organize the imports, start from python, Django, third-party apps, and your apps to make it easy to read._

9. Add below fields to Room model:

```py
name = models.CharField(max_length=140)
description = models.TextField()
country = CountryField()
city = models.CharField(max_length=80)
price = models.IntegerField()
address = models.CharField(max_length=140)
guests = models.IntegerField()
beds = models.IntegerField()
bedrooms = models.IntegerField()
baths = models.IntegerField()
check_in = models.TimeField()
check_out = models.TimeField()
instant_book = models.BooleanField(default=False)
host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
```

-  _Host_ is a owner. Since this is included in an user model. You need to connect User and Model together using a foreign key.
-  DateTimeField has a function called auto_now and auto_now_add. You can make Django update current date and time whenever a model is created or updated.
-  Please notice that the host is now connected to the user data now :)

## 3.2 Foreign key

**Foreign key is connecting one key from another.**

-  **Many-to-one**: There are many rooms to one user same as you can have many pictures for one user. This is a foreign key. Many to 1.
-  You can create 100 users but a room only points to 1 user.
-  Therefore, user is a foreign key to

## 3.3 Many-to-Many

-  What Django and Python trying to do is that they take the class and make them into a string. This is called a **string method**.
-  For example, if you do not like how the user (owners) options are displayed, you can create a custom str method on the user.

```python
def __str__(self):
    return "potato".
```

-  Create a string method on a room app.
-  **Many-to-Many**: a relationship that many things can have many things. For example, a father and a mother can have many children; user can have many rooms.

-  Create a model for amenity, facility, and dining.
-  Create a model for a type of a house.
-  Create an abstract class for Items.

rooms/models.py:

```py
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass

...
room_type = models.ManyToManyField(RoomType, blank=True)


```

-  you can create a many to many relaionships between Room and Room Types.
-  One room can have multiple RoomType and a RoomType can have multiple Rooms.
-  Admin panel provides an option to select multiple RoomTypes for a Room.

## 3.3 Create on_Delete, Amenity, Facility, HouseRule Models

-  Foreign key to the user is now created from a room.
-  If we delete from the user, what should we do?
   -  Once you delete a user, a room gets deleted. (One-to-Many - cascade effect - one effects many.)
-  Foreign key has on_delete. If you delete the user, a room will be deleted.
-  _There is no on_delete to many-to-many._

_Recap:_ Abstract item is only for naming.

**Amenity application**:

-  The important thing for a developer is to decide whether to make your code easily chaneable or not. Some functions are expected to be updated so it is good to leave things easily updatable.

-  Add a new model _amenities_ to room/models.
-  Create a relatinoship between the room type and
-  Please be familiar with the concept of inheritance. You can make bunch of things from different apps and classes.

To explain the nutshell of creating a new model within the app.

Steps:

1. Register in @admin.
   admin.py:

```py
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
```

2. Create a model classes
   models.py

```py
    """ RoomType Model Definition """

    pass


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    pass


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

```

3. Create Types of classes.
   models.py

```py
room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
amenities = models.ManyToManyField(Amenity)
facilities = models.ManyToManyField(Facility)
house_rules = models.ManyToManyField(HouseRule)
```

-  As a result, you have a blue fieldSets called Rooms. It has Amenitys, Facilitys, House Rules, Room types, and Rooms.
-  Notice that some spellings are different when the words become a plural. This needs to be manually configured.

## 3.4 Meta Class and Photos Models

-  In order to change the verbose for the name plural, we can change the class Meta > verbose_name_plural to a string variable that we want to show when it turns to plurals.
-  There are other things that you can do from the Meta class.

   -  we can change:

   1. the ordering on the form. etc

-  Since a room now has relationships with models such as a room type, amenities, facilities, and house rules, you can add from a room form.
-  _blank=true will make the data non-required._
-  Photos linked to room and the room is linked with users.
-  _You can create a foreign key with a string as well._ With this
-  Create a photo form in the room model and then register.

# 4.0 Other Apps.

## 4.1 Review Model

-  Review model have 6 items to rate from 0 to 5
   Steps:

1. Install reviews in the config/setting.py

```
under PROJECT_APPS,
ADD "reviews.apps.ReviewsConfig",
```

2. Update the reviews/models.py

```py
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.
    # User and Room are connected to reviews. If you delete the user, this review is deleted.
    User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
```

3. Register in the reviews/settings.py
4. Migrate
5. View the results

**Relationship in Django**:

-  We can get values from the connected objects with below:

```py
def __str__(self)
    return self.room;

"""
possible scenarios:
- you can navigate to three later deep with the relationship that you have.
- For ex:
    - self.room.name
    - self.review
    etc...
"""
```

## 4.2 Reservation Model

-  Guest Checking
-  Status
-  Confirm

Steps to set up:

1. Install a reservation app to config/settings.py
2. Create a new class called **Reservation** in the reservations/model.py

```py
class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
```

3. Register the app in the

## 4.3 Lists

-  lists could have many listings of places:

   -  stays
   -  places
   -  experiences

-  Creating models take the similar steps so I will skip writing out all the details.
   models.py

```py
class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
```

## 4.3 Conversations

-  Start a conversations app **Run django-admin startapp conversations**
-  Conversations contains:
   -  trip model
   -  chatbox type conversation bubble between two users.
   -  participations.
   -
