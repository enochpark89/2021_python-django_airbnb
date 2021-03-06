# Airbnb Clone

# Table of Contents:

-  This is to copy similar functional website as Airbnb with Django and Tailwind CSS etc.

# Programming languages/framework used

-  JS, HTML, CSS, Python, Django

# Software Requirement

-  [x] Python 3.0
-  [x] Django
-  [x] pipenv

_Please look at the documentation on how to install these on your particular OS system._

# Progress Journal

-  If you are serious about the career as a Django developer, we recommend using a pycharm community or a professional version.
   **Jetbrains**: The company who developed Pycharm. They have IDE for many programming languages.
-  Django vs Flask:
   **Python**: mininalistic (Flask, Pyramid), simple code; lots of manual work; invent wheels
   **Django**: a massive framework; comes with many utilities; Use other ppl's work; no need to reinvent a wheel.
-  If you use Django template, you will save alot of time building a website.
   **A rule of thumb:**: A web app that requires many user interactions should use React.
-  You do not always need to use React to build a website. It might be better in some cases to use Django.
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

1. Run _django-admin startproject config_
2. We have two folders (config, manage.py) > Take it ouside the config folder and delete the config folder that holds two files (config and manage.py).

**Additional packages**: - Linter: looks at your code and tries to foresee the errors that might come up in the future. - Flask 8 and pylint - Formatter - Black: install Black - recommend which codes to format. - PEP8: A style guide that is recommended for a clean code.
_For do DOs AND DON'T, (Please read the documentation)_

## 1.4 First look at Django

**init.py**: A starting point; init.py is needed to Everytime you make a file you need to have **init.py**.
**settings.py**: Everything is set up in the beginning to make the application that Django gives us. (Admin, Auth, ContentTypes, Sessions, Messages, Static Files, and Middlewares, WSGI, and DB.)
_Tip: Django comes with files and comments. These comments are very valuable because it explains about the pre-setting that is created._
**Django documentation**: Django documentations are available to all in the setting file. - CTRL click to see the detail of the files. - Look at comments to understand what files do.

**Manage.py**: have many commands. If you hover your mouse on, click command or control and you can enter into the related file.

-  Run _python manage.py runserver_ to start the server. The default localhost is 8000. (http://localhost:8000/)

   -  Afterwards, if you save any of the files, it will update the changed information.
   -  "/admin" shows an administrator page. It requires a login.

-  Run _python manage.py migrate_ > Chan ges on the DB is adjusted
   _Tip: Always check whether you are running the server_

-  To create a super user, you run _python manage.py createsuperuser_

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

-  Start a conversations app Run **django-admin startapp conversations**
-  Conversations contains:
   -  trip model
   -  chatbox type conversation bubble between two users.
   -  participations.

(Skipping the model setup as it is similar with other apps that we set up previously)

# 5.0 Room Admin

## 5.1 Room Admin Panel - Search

-  Create list_display from the room/admin.py

```py
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
```

-  On Airbnb, when you write a city, and it shows recommendations that the system guess what the users wrote.

-  Within admin, there are many things that you can add. (_Please refer to the Django project docs_)
   -  ModelAdmins option
      -  actions
      -  empty_value_display
      -  fields: hide the fields
      -  exlude:
      -  search_fields: enable a searchbox, with fields as arguments. It uses a regular expression to specify the search method and results.
      ```
      # search for keyword that has exact (=) city name and startswith(^)host_username
        search_fields = ("=city", "^host__username")
      ```

## 5.2 Room Admin Panel -

-  **filter_horizontal** works with many-to-many relationship.
-  Use _classes collapse_ to render collapsable sections.
-  **Ordering**: tell the admin how to order the list. You can order by different columns.

## 5.3 Custom Admin Functions

-  You can add columns by adding to list_display.
-  After adding another column, you can add another class within the admin.py. as below
-  Whatever you return in the class, the value will be shown as a field value. (column value.)

```py
def count_amenities(self, obj):
        return obj.amenities.count()
```

-  we can even change the column name by stating below

```
count_amenities.short_desciption = "new name of the column"
```

-  we can explore what kind of methods and properties **obj** has.
-  obj.amenities.all() contains the <QuerySet>

# 6.0 Models and Querysets

## 6.1 Managers and Queryset

-  With the Queryset and the object value you can create many columns that calculate the give stats of the models.
-  Activate the bubble > pipenv shell
-  Run _Python manage.py shell_: to access the Django objects.

_How do you get the object from the DB?_

-  Terms:
   Vars:
   _Def: vars returns the dict attribute for a module, class, instance or any other object with a dict attribute_
   Dir:
   _Def: dir return the list of names in the current local scope._

-  These two functions are needed to access the DB in Django.

Steps:
_Tip: CTRL+L cleans the shell terminal._

1. Vars(User):
   Uses:
   AbstractUser > AbstractBaseUser >
   Models

2. User.objects > returns <...UserManager> - UserManager get elements from the DB without using SQL.

3. If you want to all the users in DB, Run _User.objects.all()_ > returns a QuerySets.

_QuerySets:_ List of objects.

4. Run _all.user.filter(superhost=true)_, returns filtered user within the condition stated.

-  Ascending(), descending()
-  reverse() etc...

5. you can create a model and put in the queried object into the model that you created

_.get returns one object_

```
>>> e = Entry.objects.get(id=2)
>>> e.blog # Returns the related Blog object.
```

-  Remeber the users that have the foreign keys.

   -  Room > Foreign key > User

-  We can access the room from the User model using _sets_
-  Element > Foreign key points to another element.
-  The one that is being pointed can access the pointer using a foreign key.

## 6.1 Django ORM and Sets

-  You can access the DB using the sets as well as below
   ex1:

```
itnico.review_set.all()
```

-  _related names_: name can be created to refer to sets.

-  You can set the _related_name_ field within the Foreign.keyed model and use that name to call the sets.

-  One object access to foreign keys.

-  On many-to-many relationship, you can use .get() to access.

-  The more you make Django, you will understand how the objects work and what it does to access the DB.

## 6.2 Many-to-Many Sets

-  Related_names are for the target.
-

## 6.3 Finish Room Admin

rooms/admin.py

-  Create to count photos.

```python
""" Item Admin Definition"""
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

```

# 7. More Admins

# 7.0 Review Admin; Room Average

There are more tasks need to be accomplished for admins.

Steps:

1. On Users, add list_filter that checks for a super user as below:

users/admin.py:

```py
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
```

-  With the is_superuser, we may check whether the user is a super user or not.

2. Review > Add average

-  Usually for reviews, it has average of ratings that people submit.

-  Add below to reviews/models.py

```py
# Takes average of 6 variables in reviews.
def rating_average(self):
    avg = (
        self.accuracy
        + self.communication
        + self.cleanliness
        + self.location
        + self.check_in
        + self.value
    ) / 6
    return round(avg, 2)

rating_average.short_description = "Avg."
```

-  Add this value to the list_display to show it on the chart.

-  We put it in the model because we want to have it on both front and back end.

3. Rooms > Get total reviews > Get an average.

```py
def total_rating(self):
all_reviews = self.reviews.all()
all_ratings = 0

for review in all_reviews:
    all_ratings += review.rating_average()
return all_ratings / len(all_reviews)
```

# 7.1 Reservations Admin

1. Create Check-in an out function

-  Import timezone from django.util.
-  Create in_progress() and is_finished() functions that compare the time now with check_in and check_out time to show a boolean value.

reservations/models.py

```py
# Get time now and if now is in between check_in and check_out time, return true for in_progess.
def in_progress(self):
    now = timezone.now().date()
    return now > self.check_in and now < self.check_out

in_progress.boolean = True

def is_finished(self):
    now = timezone.now().date()
    return now > self.check_out

is_finished.boolean = True
```

# 7.2 Conversions, Lists, Reservations Admin

-  Count the number of stays

Steps:

1. Update lists app:

lists/models.py

```py
def count_rooms(self):
    return self.rooms.count()

count_rooms.short_description = "Number of Rooms"
```

lists/admin.py

```py
list_display = ("name", "user", "count_rooms")

search_fields = ("name",)

filter_horizontal = ("rooms",)
```

2. Create messages and participants counts.
   conversations/admin.py:

```py
    """ Message Admin Definition """

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")
```

## 7.3 User Upload

-  When the admin click on the photo, it shows that the photo is not found.

   -  User media_root to handle the media files.

-  We can make photos be uploaded into the server path.

-  Set the path.

config/settings.py

```py
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
```

-  Change the model.ImageField()

rooms/models.py

```py
file = models.ImageField(upload_to="room_photos")

```

-  Since the stored file is not for public, use MEDIA_URL to handle the media served.

   -  This is telling Django to go to this URL when they are trying to handle or serve any media requests.

-  Now, the URL seems complicated because of the relative paths.

config/settings.py

```py
MEDIA_URL = "/media/"

```

**WARNING: Please note that it is NOT a good practice to save files in the servers.**

-  you rather save in the seperate file storage because the server - production environment, they tend to create replica would might result in replicating the private data.

   -  store in Amazon S3 instead.

-  Whenever you are importing the setting in the config, we do not import the file but you import the mirror of the file.

config/settings.py

```py
from django.conf import settings
from django.conf.urls.static import static

# If DEBUG is true, which indicate you are in the development, you will get the files from the local server.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

_static_: it helps us serve the static file.

-  After you implement the codes, you will see the URL that is without relative URL.
   -  We connect the URL with the folder.
   -  Later, we will change this path the the Amazon Storage.
   -  We do not even want the DB in our server. We need a seperate DB.

## 7.4 Photo Admin

-  Create get_thumbnail.

-  obj.file has many properties like field, file, height, url, width, and others.
   -  use obj.file.width and obj.file.height etc.

```py
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

```

## 7.5 raw_id and inline Admin

-  raw_id_fields give opportunity to look at the foreign key in a better way.
-  if you click on the host, it takes you to the small winodw that shows a list of hosts.

-  Rooms have photosets. Room > Photo > Add photo is easy.

-  Use inlineModelAdmin to put admin inside a different admin.

-  With inlineModelAdmin, Django creates blue fields, caption, File, Delete options to upload photos. Since the relationship is created between the room and the photos. The room knows where to store the file.

## 7.6 Python super()

-  Need to intersect save() method.
-  We need to intercept the fields after the user SAVE this data. We have to retrieve the fields in the middle and format accordingly.
-  To do this, we have to understand what super() is in OOP.
   -  Dog -- inherit --> puppy
   -  if
      **With super(), we can extend the method of a parent class.**

## 7.6 Python super()

-  DB documentation Model has everything about the models and methods.
-  Django admin and model both have save admin.
-  When you save the model from anywhere, the save technique is going to be used because it has to check the format of fields before saving.
-  save_model(self, request, obj, form, change)
   -  all the properties are what you can print and modify.
   -  these give more control to admins.
-  For example, if there are 5 admins and 1 does not save, all the admins wanted to notify for the saving. you can but send_mail() notification on the save_model class.

```py
# Make the first letter of the city field capitalized.
def save(self, *args, **kwargs):
    self.city = str.capitalize(self.city)
    super().save(*args, **kwargs)

```

# 8.0 Costom Commands and Seeding

-  DB seems empty. Programmers do not want to create dummy variables by clicking.
-  you can create your own command in python.
-  We can use django-seed to create fake data as fast as you can.

-  We need to create custom commands because we want to automate putting data to our DB instead of manual clicking.

Creating custom commands:

1. Django has a documentation about creating custom commands. Since Django already has some tools to create custom commands, please read the part that you need.
2. Go to any apps, create a folder called "management"
3. Inside the folder "management," create "**init**.py" file and "commands" folder.
4. If you create .py inside the "commands" folder, you may utilize this commands from python for the project.
5. In this particular example, "loveyou.py" was used.
6. Create a baseCommand which is provided by Django to easily create a custom command.
7. "help" is to explain to users what this command do.
8. "add_arguments" add arguments that the user can input for a custom command (ex: --time will take integer for the argument called "times".
9. This argument can be used in handle() function to perform an operation.
10.   This particular case, Nicolas decided to create an operation that repeats a string "I love you" by argument "times" ("I love you" \* "times")
11.   In thoery, any operations can be done inside handle() for multi-purposes.
      room/managements/commands/loveyou.py:

```py
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
```

## 8.1 seed_amenities command

-  seed_amenities interact with the Model amenities and create Amenity objects.

1. seed_amenities have array of dummy variables.
2. seed_amenities interact with Amenity model in rooms app. (imported)
3. handle() function will iterate through the amenities array with dummy values and create Amenity objects.
4. when you run command "python manage.py seed_amenities," 50 Amenity objects gets created instantly.
5. This is useful because for testing purposes, 50 objects had to be created. Without a custom command "seed_amenities," administrator would have manually created 50 Amenity objects by clicking which could take considerable time.
   I hope this helps! God bless you all :)

_Please refer to seed_amenities.py for this command_
seed_amenities:

```py
from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):

    help = "This command creates many users"

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))

```

## 8.2 seed_everything and seed_users.

1. Create dummy objects for facilities model
2. Download Django-seed
3. Add to the config/settings as a third-party apps.
4. import and use it to fill out random fields for testing.

seed_user.py:

```py
class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
```

## 8.2 seed_rooms

-  seeder doesn't help with the forign key.
-  you have to get the users from the User model for th Host field.
-  Django_seed uses faker. It creates fake data.

```py

def handle(self, *args, **options):
    number = options.get("number")
    seeder = Seed.seeder()
    all_users = user_models.User.objects.all()
    room_types = room_models.RoomType.objects.all()
    seeder.add_entity(
        room_models.Room,
        number,
        {
            "name": lambda x: seeder.faker.address(),
            "host": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "guests": lambda x: random.randint(1, 20),
            "price": lambda x: random.randint(1, 300),
            "beds": lambda x: random.randint(1, 5),
            "bedrooms": lambda x: random.randint(1, 5),
            "baths": lambda x: random.randint(1, 5),
        },
    )
```

## 8.3 reviws

-  similar as beofre

## 8.4 seed_list

-  when you are trying to add multiple-to-multiple values, you have to use flatten as below

```py
created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
```

## 8.5 seed_reservation

-  For the conversation, there is no point faking the message because this is the one that only logged in user can have.

-  Reservation is similar as the others that we've done before. _Please check seed_reservation.py for detail._

# 9.0 Views and URLs.

-  URL is a path, and view is a way you answer the request.

1. On rooms/views, create a function called all_rooms(request):
   pass.

rooms/views.py

```py
def all_rooms(request):
    pass
```

2. On config/url, import the views from the room, and create urlpatterns as below:
   config/url.py

```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
```

3. To prevent url.py getting too big, it is good idea to divide url codes into different loctions.

-  all the url that starts with /rooms > room app
-  /users > users app.
-  All the others, put them in core.

4. Manually create url.py inside the core app and update as below:

```py
from django.urls import path
from rooms import views as room_views

# app needs to be specified because Django is going to complain.
app_name = "core"

urlpatterns = [path("", room_views.all_rooms, name="home")]
```

# 9.1 HttpResponse and Render

-  _How does the views work?_
-  Go to a view, you are making an HttpRequest and this has to be responded with HttpResponse.

-  If we do not return the HTTP request, we will get an error message and the user's browser will be waiting and pending.

-  HTTP request is valuable because we can check the userLoggedIn, Form, PW, ID, information etc.

-  If we print() the request, we notice that the request is WSGIRequest.

-  print(vars(request)) will show all the methods and properties inside the request.

-  if we do not have a request, we cannot respond.

-  returning a response could be simple as below

```
return HttpResponse(content="hello")
```

-  However, if you want to return HTML element, you can user render() function as below:

```py
    return render(request, "all_rooms")
```

-  Though you can send the content by the HTML tags, we are not going to do this because it is too elementary and doesn't look good on the code and the page. Instead, we can return the HTML template as a whole to display to the user.

# 9.2 Django Templates

-  Though we responded with HTTP respond, we do not want to respond with HTTP respond every time.
-  We rather use templates.

1. Create a folder named templates.
2. Create an all_rooms.html file under templates folder.
3. Let Django know where to look for the templates.
4. config/settings.py
   under TEMPLATES var, add below:

```py
        "DIRS": [os.path.join(BASE_DIR, "templates")],
```

5. We can send many variables along with the template as below
   rooms/views.py:

```py
def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
```

6. For the HTML file, you can use the variables that was sent along with the HTTP response as below:

```html
<h1>Hello!!</h1>

<h4>The time right now is: {{now}}</h4>

<h6>{% if hungry %}I'm hungry{% else %}i'm okay{% endif %}</h6>
```

-  The curly bracket and percentage "{%  %} to use the python code and logics
-  The double curly brackets to use the variables sent from HTTP response.

7. Extend templates from other models.

-  you can get rooms from the Django DB.
-  import the models and use in views.py

```py
from django.shortcuts import render
from . import models

# Create your views here.
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"potato": all_rooms})

```

-  To display all the room.name you do below on the home template.
   home.html

```html
{% extends "base.html" %} {% for room in potato %}
<h1>{{room.name}} / ${{room.price}}</h1>
{% endfor %}
```

8. Create base.html under rooms folder to reduce repetition.

-  blocks are way that children template can put info in the parent template.

base.html

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta http-equiv="X-UA-Compatible" content="ie=edge" />
</head>
<body>
{% include "partials/header.html" %}

{% block content %}{% endblock %}

{% include "partials/footer.html" %}
</body>
</html>
```

home.html

```html
{% extends "base.html" %} {% block page_name %} Home {% endblock page_name %} {%
block content %} {% for room in potato %}
<h1>{{room.name}} / ${{room.price}}</h1>
{% endfor %} {% endblock content %}
```

-  They are connected by extending so you can use each other's parts. In the same way, you can create both footer and header.

_Please refer to templates/partials/footer.html and header.html for detail_

-  We are not suppose to show all the objects to the users because it gives too much burden on DB. Therefore, we show 10 information at a time.

# 10 HomeView

-  Since there are many objects showing, we will make it show only 10 at a time. There are three ways of doing it:

1. 100% manual with python.
2. Little help from Django.
3. Make a view with no code.

-  When you research, people only teach shortcuts. If you are too exposed to shorcuts, you will not know how exactly Django works on the backend.

# 10.1 Pagination with Limit and Offset

-  The approach we can take is to take the object.all() query and get 10 each objects using [0:10]. When the page loads, we have to increment the numbers by 10.

```py
    return render(request, "rooms/home.html", context={"potato": all_rooms}[0:10])
```

-  For the pages, we change change the url to display a new page each time an user click next pagination button.
   -  page is navigated with the "localhost/?page=<number>" format
-  Query dictionary has get() function. (ex: requests.GET.get()) - with this function, it will read where the user is in different URL page.
   rooms/views.py

```py
from django.shortcuts import render
from . import models

def all_rooms(request):

    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", {"potato": all_rooms})

```

-  Two errors:
   1. Empty page error.
   2. The page doesn't exist.

# 10.2 Pages List Navigation

-  Fix two errors suggested:

1. If there is no page returned, it will resolve in an error. In order to avoid this error, we can set the default value of a page as below:

views.py

```py
page = request.GET.get("page", 1)
page = int(page or 1)
```

2. Display the page on the bottom of the page.

home.html

```py
<h5> Page {{page}} of {{page_count}}</h5>
```

3. Create a page navigation links on the bottom that shows all pages to navigate.

-  Assuming that the page_range variable was rendered from views.py, use below:
   -  Basic logic:

home.html

```py
    {% for page in page_range %}
        <a href="?page={{page}}">{{page}}</a>
    {% endfor %}
```

# 10.3 Next Previous Page Navigation

-  Instead of doing list to present pages, we are going to change to _Previous_ and _Next_ buttons.
-  With a Django function template filter and tags, you can easily create Previous and Next buttons.
-  Make sure to set a limit so that uses can't go more than the maximum pages. (ex: ?page={{page|add:-1}})

rooms/home.html

```html
<h5>
   {% if page is not 1 %}
   <a href="?page={{page|add:-1}}">Previous</a>
   {% endif %} Page {{page}} of {{page_count}} {% if not page == page_count %}
   <a href="?page={{page|add:1}}">Next</a>
   {% endif %}
</h5>
```

-  finished room/view.py

```py
from django.shortcuts import render
from . import models
from math import ceil

# Create your views here.
def all_rooms(request):

    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    # limit of how many objects are displayed.
    limit = page_size * page
    offset = limit - page_size
    # This limit and offset is designed to make limit = limit-10 so that it will only display 10 objects at a time.
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )

```

# 10.4 Django Paginator

-  Django always try to take repetitive/menial tasks and help developers.
-  Django has a library called paginator.

Steps:

1. Import paginator from Django.core.paginator.
2. Use paginator to get limited number of objects at a time.
   rooms/views.py:

```py
# Paginator will get 10 room_lists from the Room models.
paginator = Paginator(room_list, 10)
rooms = paginator.get_page(page)
```

3. Render rooms objects to the home.html so that all the method within the rooms can be used.

rooms/views.py with Pagination

```py
from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.
def all_rooms(request):

    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    # Paginator will get 10 room_lists from the Room models.
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms": rooms})

```

```html
{% extends "base.html" %} {% block page_name %} Home {% endblock page_name %} {%
block content %} {% for room in rooms.object_list %}
<h1>{{room.name}} / ${{room.price}}</h1>
{% endfor %}

<h5>
   {% if rooms.has_previous %}
   <a href="?page={{rooms.number|add:-1}}">Previous</a>
   {% endif %} Page {{rooms.number}} of {{rooms.paginator.num_pages}} {% if
   rooms.has_next %}
   <a href="?page={{rooms.number|add:1}}">Next</a>
   {% endif %}
</h5>

{% endblock content %}
```

-  notice rooms.paginator.num_pages give the total number of pages retrieved from the models. Since the maximum pages is specified, it will do the calculation of its own to show the total number of pages possible.
-  There are many others like invalid_pages, methods, page.has_pages etcs.

# 10.5 Reviews, get_pages, and page

_Recap:_

1. Created a room_list
2. Created a Paginator that takes in two arguments
   a. list of objects
   b. number of items in a page.
3. We have two methods _get_page_ and _page_.
   -  get_page returns a page object.
   -  .page() does a similar things
   -  page objects have many methods and attributes such as has_next, has_previous, has_other_pages, etc.
   -  attributes: .pagination - it has a reference to the father.
4. However, if we change to display the previous and next page with this function _page.previous_page_number_ and _page.next_page_number_, then the error will show up if there is no next or previous page available.

5. Often times, hacker wants to put a wierd variable to the page or fields.
   _orphans: list of elements that are not big as the page._

-  you can set the orphan arguments.

6. Set the orphan to 5 (_how many organs do you want to hide?_). Then, the past page will contain 15 elements or objects.

7. int(page()) to protect the field from a wrong type.
8. In conclusion, get_page has less control but many premade featueres but page has more controls but less premade features.

-  We have to fix the error when there is an empty page but this is the final views.py.

```py
{% extends "base.html" %}
{% block page_name %}
    Home
{% endblock page_name %}
{% block content %}

    {% for room in page.object_list  %}
        <h1>{{room.name}} / ${{room.price}}</h1>
    {% endfor %}

    <h5>
    {% if page.has_previous %}
        <a href="?page={{page.previous_page_number}}">Previous</a>
    {% endif %}

    Page {{page.number}} of {{page.paginator.num_pages}}

    {% if page.has_next  %}
        <a href="?page={{page.next_page_number}}">Next</a>
    {% endif %}

    </h5>

<!-- pagination by numbers of pages.
    {% for page in page_range %}
        <a href="?page={{page}}">{{page}}</a>
    {% endfor %} -->

{% endblock content %}
```

# 10.6 Handling Exceptions

-  When the user puts a page number that is not available on the url, we can redirect users to home.
-  Python is really good with exceptions.
   _Tip: construct your error handler as if error happens try A, B, C rather than make a specific error handler for a specific situation._

Final update on rooms/views:

```py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    # Paginator will get 10 room_lists from the Room models.
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
```

# 10.7 Class Based Views

-  **list view:**
   -  comes from a class > class based view - abstract.
   -  A page representing list of objects.
   -  Using list view, with no programming, it does the job of making paginations.

1. Import ListView from django.views.generic

   -  path() only takes an url and a function.
   -  Since ListView has a method, as_view(), that turns into a fucntion.

_Tip: Use ccbv.co.uk to explore ListView methods easily._

2. With premade functions or methods, you can create pagination and ordering as below:

rooms/view.py

```py
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

```

-  you have to change the home.html to templates/rooms/room_list.html in order to use the ListView functions.

3. Alternative List View.

-  Some people believe that this is too magical, and the logic of the code should be easily readable.
-  There are on-going debates between functions or classes.
-  We should be able to choose wisely and flexibily depending on projects that we use.
-  The basic rule of thumb:
   a. listing something - use inheritance - ListView
   b. Complicateed form with filtering and login form - use functionbased views.
-  all of them have ListView > get_context_data. > super.context_data.

views.py

```py
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
```

templates/rooms/room_list.html

```py

{% block content %}

    {{now}}

    {% for room in rooms  %}
        <h1>{{room.name}} / ${{room.price}}</h1>
    {% endfor %}

```

# 11.0 Detail View

Two things to learn about the URL:

1. Django path package allows you to have variables on the path.

```py
urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
```

2. Django's url can be displayed as below to access the Detail view.

```py
    {% for room in rooms  %}
    <h3>
        # This part leads to the /rooms/detail URL path.
        <a href="{% url "rooms:detail" room.pk %}">
            {{room.name}} / ${{room.price}}
        </a>
    </h3>
    {% endfor %}
```

# 11.1 get_absolute_url

-  In order to view how each app is being displayed on the web, we can use get_absolute_url. This creates a button on the website to "view on website."

models.py:

```py
def get_absolute_url(self):
    return "/potato"
```

-  _reverse_ is a function that takes the name of the url and returns the actual url.

```py
def get_absolute_url(self):
    return reverse("room:detail", kwargs={"pk": self.pk})
```

# 11.2 room_detail FBV finished

-  detail needs to provide information about the room.

1. Modify the rooms/models.py to have _from django.urls import reverse._
2. Modify the rooms/views.py as below:
   rooms/views.py:

```py

def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))

```

3. Modify detail.html to show details of the room.

```html
{% extends "base.html" %} {% block page_name %} Home {% endblock page_name %} {%
block content %}
<div>
   <h1>{{room.name}}</h1>
   <h3>{{room.description}}</h3>
</div>
<div>
   <h2>
      By: {{room.host.username}} {% if room.host.superhost %} (superhost) {%
      endif %}
   </h2>
   <h3>Amenities</h3>
   <ul>
      {% for a in room.amenities.all %}
      <li>{{a}}</li>
      {% endfor %}
   </ul>
   <h3>Facilities</h3>
   <ul>
      {% for a in room.facilities.all %}
      <li>{{a}}</li>
      {% endfor %}
   </ul>
   <h3>House Rules</h3>
   <ul>
      {% for a in room.house_rules.all %}
      <li>{{a}}</li>
      {% endfor %}
   </ul>
</div>
{% endblock %}
```

4. If there is no room information, redirect users to the home site.
   _reverse is recommended in this process._

# 11.3 HTTP 404() code.

-  404 page is to let the browser understand the outcome of a request.

1. Import HTTP 404 package.

rooms/views.py:

```py
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from . import models

        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # Raise an error instead of returning.
        raise Http404()
```

2. Create a HTTP 404 template.

   404.html:

```py
{% extends "base.html" %}

{% block content %}

    <h1>Sorry! The page is not found.</h1>


{% endblock content %}
```

3. Update config/settings.py DEBUG value to False, and ALLOWED HOSTS value to all("\*")

```py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = "*"
```

-  In conclusion, if the user enters a room number that does not exist, it will raise an 404 error.

# 11.4 Using DetailView CBV

-  We created a function-based view. We are going to change to class-based view. Please decide for yourself which one is better.

1. Update rooms/views.py:

```py
from django.views.generic import ListView, DetailView
from . import models
# Class-based View
class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room

```

2. Update urlpatterns value in rooms/urls.py to use RoomDetail.as_view().

rooms/url.py

```py
urlpatterns = [path("<int:pk>", views.RoomDetail.as_view(), name="detail")]
```

3. In config/settings.py, change DEBUG to True, and ALLOWED_HOSTS to [].

-  Everything works the same as the functional-based View.
   Summary:
   a. On the View Template, you can use the object name or the app name.
   b. Django by default is going to look for the URL element pk as it is stated in urlpattern, and View class RoomDetail.
   c. In a nutshell, it is a communication from URLS.py > Views.py > View Template.

# 12.0 Search View

-  Search View

1. create a def search() in views.py.

rooms/views.py:

```py
def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
```

2. Create a search.html template that shows the result of a search.
   search.html:

```py
{% extends "base.html" %}

{% block page_title %}
    Search
{% endblock page_title %}

{% block content %}

    <h2>Search!</h2>

    <h4>Searching by {{city}}</h4>

{% endblock content %}
```

3. Update urls.py to route the user to a /search page.

```py
path("search/", views.search, name="search"),
```

4. Update navbar to include to search form.

template/partials/nav.html.

```html
<form method="get" action="{% url "rooms:search" %}">
    <input name="city" placeholder="Search by City" />
</form>
```

5. Show the search result when users submit a form.

# 12.1 Start the form

1. Modify the forms so that the searchbar from the base.html wouldn't show on the search result page.

-  USE {% block %} to accomplish this

template/base.html

```py
<header>
    {% include "partials/nav.html" %}
    {% block search-bar %}
    <form method="get" action="{% url "rooms:search" %}">
        <input name="city" placeholder="Search By City" />
    </form>
    {% endblock search-bar %}
</header>
```

templates/rooms/search.html:

```py
# Add below block since this is included in base.html.
{% block search-bar %}
{% endblock search-bar %}
```

2. Add more fields to search in View.

rooms/views.py:

```py
# Add room_types field so that the users can search.
room_types = models.RoomType.objects.all()
return render(
    request,
    "rooms/search.html",
    {"city": city, "countries": countries, "room_types": room_types},
)
```

-  As a result, when an user searches, it will autopopulate the keyword that they search with more options.
-  Please put value so that the keyword will be shown on the URL as an user searches.

## 12.2 Select Choices

-  Update the View to add more choices.

rooms/views.py:

```py
def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = request.GET.get("country", 0)
    room_types = models.RoomType.objects.all()

    # What we get from a form
    form = {"city": city, "room_type": room_type, "country": country}

    # What we get from a DB.
    options = {"countries": countries, "room_types": room_types}

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )

```

-  Update the selected choices to appear on a form as below:

```html
<form method="get" action="{% url "rooms:search" %}">
    <div>
        <label for="city">City</label>
        <input value="{{city}}" id="city" name="city" placeholder="Search By City" />
    </div>

    <div>
        <label for="country">Country</label>
        <select id="country" name="country" >
            {% for country in countries  %}
                <option value="{{country.code}}" {% if country.code == selected_country %}selected{% endif %}>{{country.name}}</option>
            {% endfor %}
        </select>
    </div>

    <div>
        <label for="room_type">Room Type</label>
        <select id="room_type" name="room_type" >
            <option value="0" {% if seleted_room_type == 0 %}selected{% endif %}> Any kind</option>
            {% for room_type in room_types  %}
                <option value="{{room_type.pk}}" {% if selected_room_type == room_type.pk %}selected{% endif %}>{{room_type.name}}</option>
            {% endfor %}
        </select>
    </div>
    <button>Search</button>
```

## 12.3 Amenities and Facilities Form

-  Adds more forms to the Search.
-  Add more inputs in search.html.

_Please refer to the Search.html and rooms/views for more detail._

## 12.4 Finish the form

-  The problem showed that the .get does not the get the list of selected amenities and facilities.
-  Instead, we can use **get_list** function to get the list.
-  sluggify makes everything into the text.
-  Add instant and super_host fields bolean to check.

## 12.5 Filtering

-  Use the field LOOKUP functionality in Django to help filter the search results.
-  There are conditionals with LOOKUP because sometimes, the search result needs to search by comparing the exisitng data. ( ex: price higher or lesser than this.)

## 12.6 Use Django form to make lives easier.

-  If you use Django form, it is easy implementation without having to write a long manual code.

-  Thanks to Django **The Forms API**!!

-  Logic: Forms.py created > Views.py imports fields from forms.py > template shows what was stated in the form.

forms.py:

```py
from django import forms
from . import models
class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(queryset=models.RoomType.objects.all())
```

views.py:

```py
def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})

```

search.html:

```html
    <h2>Search!</h2>

    <form method="get" action="{% url "rooms:search" %}">
                {{form.as_p}}
        <button>Search</button>
    </form>
    <h3>Results</h3>
    {% for room in rooms %}
        <h3>{{room.name}}</h3>
    {% endfor %}
{% endblock content %}
```

## 12.7 Forms extended fields

-  If you want to show more fields on the search form, you can just add the fields in the forms.py. However, please note that fields must exist in Model.

-  Django uses help_text. (ex: If you state the help_text under the Model fields, it will show users on the input fields.)

## 12.8 Make the Form remember the keywords.

-  The form is going back with the list of errors by default.
-  Once we give a form data, it will automatically tries to validate the data. (bounded form > validate data)
-  In order to prevent errors, you make the required property false on the form.

_Benefit of a form_

1. Creates HTML really quickly
2. Clean the data.

-  urls.py should point to the SearchView.
-  views.py should use the form.cleaned_data to validate data with the name SearchView.

```py
class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                rooms = models.Room.objects.filter(**filter_args)

        else:

            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form, "rooms": rooms})

```

## 12.9

# 13.0 Login form

-  The login forms and autentication need to be created, but it is easy with Django because it comes with features that help this process.

# 13.3 Validate data

-  Added the initial value for convenience; added render to render a page after the login.

1. Use clean_email() to clean, validate

-  if you just return the clean_email, the value will not be returned.

-  Validate email and password and must return values.

forms.py:

```py
class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check for the existing user. Otherwise, raise an error.
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

```

2. Use clean_password() to clean the data.

-  Get the user and use check_password() method

```py

# Clean password.
password = self.cleaned_data.get("password")

try:
# Find user; check passwords
user = models.User.objects.get(email=email)
if user.check_password(password):
    return self.cleaned_data
else:
    self.add_error("password", forms.ValidationError("Password is wrong"))
except models.User.DoesNotExist:
self.add_error("email", forms.ValidationError("User does not exist"))

```

3. Change the clean() instead of cleanEmail and clean both password and email.

_Always need to return clean_data as 'self.clean_data'_

# 13.4 Authenticate Logins

-  using Django library autenticate and login, we can authenticate and check login information.

1. In a View, import authenticate, login, logout libraries.

2. Use authenticate to authenticate both username and passwords.

```py
user = authenticate(request, username=email, password=password)
```

3. If authenticated, login the users

```py
if user is not None:
    login(request, user)
    return redirect(reverse("core:home"))
```

4. Use a logout library to logout the user as below:
   view.py

```py
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
```

5. Include urlpatterns to have the logout path.

urls.py

```py
urlpatterns = [
path("logout", views.log_out, name="logout"),
]
```

6. Include the option to login and logout on the template

-  Django uses a **context Processor**.
-  Takes a cookie, look for the user and put the user in the template.
-  is a Python Function that takes one argument and returns a library.
-  in a nutshell, the user is found when they login and make the login text to logout.

nav.html:

```py

    {% if user.is_authenticated %}
        <li><a href="{% url "users:logout" %}">Log out</a></li>
    {% else %}
        <li><a href="{% url "users:login" %}">Log in</a></li>
    {% endif %}

```

7. Create logout function in view.py

```py
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

```

# 13.5 An easier way to authenticate and create login forms.

-  Use loginView that creates a login form and takes care of the authentication.

-  Use logoutView to let the user logout.

-  _Please read a Django documentation_

# 14.0 Sign up form

-  Sign up form is required for new users.

1. Create an anchor element in the template so that users are directed to the form page.

2. On urls.py, add thew SignUpview to urlpatterns.

urls.py:

```py
    path("sigup", views.SignUpView.as_view(), name="signup"),
```

3. Add SingUpView class in views.py

```py
class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "Nicoas", "last_name": "Serr", "email": "itn@las.com"}
```

4. Inside the SignUpView, create form_class that takes the form template from the forms.py.

forms.py

```py
class SignUpForm(forms.Form):

    # Field specifications:
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
```

5. Create Save(self) function under the form that saves the data.

-  We need to encrypt the password.

6. Update the view.py that validate the data and authenticate the login account.

-  create form_valid(self, form) that validates and authenticate the user login form.

-  ModelForm basically connects Model and Form so that we do not have to create different fields manually.
-  it validates the uniqueness of the data.

_Please read about the ModelForm from the Django website._

-  If you use ModelForm, the form.py gets simplified.

   -  No clean_email(self)
   -  save takes arguments, and keyward arguments.

-  form_valid function from Views.py gets simplier.

```py
def form_valid(self, form):
    form.save()
```

-  "commit = false" means do not save on the db.

# 15.0 Verify Email

-  Need to create an email server to send an email because email providers will put the regular server to a spam to protect people from spams.

1. Create an account in mailgun.com
2. Look at Domain and SMTP credentails.
3. According to Django Documentation, HTTP host and port need to be specified.
4. Include the email configuration under config/settings.

config/settings.py:

```py
# Email Configuration

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = "587"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
```

# 15.1 Dotenv

-  You do not want to save the passwords in the source code.

1. Install Django-dotenv.

-  include .env file > include mailgun username and passwords in there.

2. Create .env file in the workding directory.

-  .env should include both the username and passwords.

3. Install Django-dotenv.

-  Run pipenv install

4. Import dotenv in the manage.py

5. Add a new values (email_confirmed and email_secret) in a model.

users/models.py

```py
email_confirmed = models.BooleanField(default=False)
email_secret = models.CharField(max_length=120, default="", blank=True)

def verify_email(self):
    pass
```

-  make migrations.
-  Need to write a logic that uses the email_confirmed and email_secret to authenticate and then send emails.

# 15.2 Verify Email

-  Finish up the def verify_email() to work on the logic.

-  you have uuid.uuid4() which gives a unique id for an email. you can make that into a hex by using uuid.uuid4().hex

1. Import uuid, settings from django.conf, send_mail from django.core.mail.

2. Finish the verify_email() function

models.py:

```py
def verify_email(self):
    if self.email_verified is False:
        secret = uuid.uuid4().hex[:20]
        self.email_secret = secret
        send_mail(
            "Verify Airbnb Account",
            f"Verify account, this is your secret: {secret}",
            settings.EMAIL_FROM,
            [self.email],
            fail_silently=False,
        )
    return
```

3. Set up Email_from to create a no-reply email

config/settings.py

```py
EMAIL_FROM = "enoch@sandbox2b6f7df484464ec08cd86345f44e3eee.mailgun.org"

```

4. Use send_mail to send email to people. _Please check the format of the send_mail package_

# 19.0 Tailwind CSS

-  Tailwind CSS has many CSS properties as a class.
-  Tailwind is good because you do not have to know much about CSS.
-  You don't have to waste time creating a new class name.
-  For example, Marketing tag is combination of many classes.
-  We can create our own button and CSS using the tailwind @apply.
-  @apply needs to be used many times to
-  _Preflight_: Tailwind comes with many of the colors and styles already.
-  Tailwind does not dictate your design. It is mostly help.
-  _Tailwind CSS_ intellisense on VSC will give recommendations and show you what classes in Tailwind means.

## 19.1 Tailwind CSS

-  Since the browser does not understand the post CSS, we need to install gulp to make the browser smart enough to understand.

_Tip:Please read the Tailwind documentation to install._

-  Install gulp by running below code > package.json and node_modules populate.

1. Run below:

```ps
npm install gulp gulp-postcss gulp-sass gulp-csso node-sass --save-dev
```

2. Set up Tailwind CSS.

-  Add node_modules/ to gitignore.

-  Install Tailwind CSS with the below code:

```powershell
npm install tailwindcss --save-dev
```

3. Set up Gulp.

a. Create a new file called gulpfile.js
b. Copy and Paste below code

```js
const gulp = require("gulp");

const css = () => {
   const postCSS = require("gulp-postcss");
   const sass = require("gulp-sass");
   const minify = require("gulp-csso");
   sass.compiler = require("node-sass");
   return gulp
      .src("assets/scss/styles.scss")
      .pipe(sass().on("error", sass.logError))
      .pipe(postCSS([require("tailwindcss"), require("autoprefixer")]))
      .pipe(minify())
      .pipe(gulp.dest("static/css"));
};
exports.default = css;
```

4. Install autoprefixer
5. Create a script that runs the CSS.

In a nutshell, Gulp is going to translate from SCSS to CSS.

-  If you run _npm run css_, the updated css will be created under static/css folder. With this, we can implement on the base.html template for use.

## 19.2 Static Files on Django.

-  In order to allow users to access the static file, we have to update the config/settings.py

1. Add below to config/settings.py

```py
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
```

2. import the CSS in the template/base.html

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}" />
```

# 20.0 Make it all Beatiful

-  Use TailwindCSS to save some time with the styling.

# 20.1 Sizes in Tailwind

-  _Sizes:_ there are percentages and rem.
-  em is a measurement.
-  rem is a root em. It cares about the closest font size. It cares about the rootsize and bases its measurement by the root.

# 20.2 Header

-  Container is like a box

   -  size with the max-width.
   -  w is width; h is height.
   -  m is margin
   -  ml is margin left
   -  there are colors too
   -  p is padding.

-  _Please refer to the Tailwind CSS documentation for detail_

## 20.3 Extending Tailwind CSS

-  You can customize the class by putting the new properties under tailwind.config.js.

# 23 UPDATE ROOM, CREATE ROOM, ROOM PHOTOS (This needs to be updated to different chapter numbers)

# 23.0 Update Room View

-  With UpdateView, just by having the pk arguments and templates, you can create a update form easily.

-  The problem is insecurity. If you go to another room, people can enter this edit url directly instead of using the buttons to edit. This is not good for security.

# 23.1 Room Photos pt.1

-  UPDATE view takes the pk in the url and takes the model and try to find one. It does not verify the ownership of that.
-  Please use get_object to verify the editability.
   a. Takes pk from the url. If yes, filter by pk.
   b. Try to get the queryset.get() room, if not there, it is going to create 404 page.
   c. We need override so that if the user is the owner, we return the room. If not, we return HTTP 404.

```
room = super().get_object(queryset=queryset).
print(room.host.pk, request.user.pk)
# returns the room host and request user. We need to compare them.
```

-  Django is not good for interface.

1. Edit photos link can be created in url.py.
2. Edit and photos are manually handled. There is Edit-photos tab.
3. Get the photos and the room.

-  Change the views.py > Create a class RoomPhotosView > takes two argument about details and photos > Use get object to display the information in the arguments > Users are seeing the photos.
-  class RoomPhotosView(user_mixins.LoggedInOnlyView, View).

4. In the templates, we create the space where we display photos and details.
5. Create a template called room_photos.html
6. Connect a template in url.py with the class.
7. In room_edit.html, create a button to edit photos.
8. In the template, you can decide how users can edit/show photo.

-  Container that holds the photos.

9. You can incorporate the values imported from other models by doing below:

Room Photos:

```py
{% extends "base.html" %}

{% block page_title %}
    {{room.name}}'s Photos
{% endblock page_title %}

{% block search-bar %}
{% endblock search-bar %}

{% block content %}

    <div class="container mx-auto my-10 flex flex-col">

        {% for photo in room.photos.all  %}
            <div class="mb-5 border p-6 border-gray-400 flex justify-between">
                <div class="flex items-start">
                    <img src="{{photo.file.url}}" class="w-32 h-32" />
                    <span class="ml-5 text-xl">{{photo.caption}}</span>
                </div>
                <div class="flex flex-col w-1/5">
                    <a class="btn-link mb-5 bg-teal-500" href="#">Edit</a>
                    <a class="btn-link bg-red-600" href="#">Delete</a>
                </div>
            </div>
        {% endfor %}

    </div>
{% endblock content %}
# Show pictures, texts, borders, paddings, buttons, there are some skills needed to create a sizeable, a good buttons and displays.
```

10.
