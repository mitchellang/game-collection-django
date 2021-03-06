# Game Collection
A simple Django application as an experimental project

## Starting the application

Please make sure you have the python library ***Django*** installed
This prototype was tested using the Anaconda supplied Python binary; version 3.7.7

To install Django using conda you can type the following command:

```
conda install -c anaconda django
```

Please follow the prompts until Django is successfully installed.

Additional advice on how to install Django can be obtained from Django's website \
https://docs.djangoproject.com/en/3.1/topics/install/

To start the Django server, move into the application directory containing the "manage.py" file

In this location run the following command:

```
python manage.py runserver
```

This should prompt you with:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 10, 2020 - 12:54:41
Django version 3.0.3, using settings 'game_management_system.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

This means the application server is running on your local machine.
Open the application in a web-browser by pasting the hyperlink http://127.0.0.1:8000/

## Creating a login

The application requires each user to create a login. 

The other pages will not render until this has been completed.

If you have not logged in before you should click on the "Sign up" link, where you can sign up.

Fill up the form and submit, then you can use the credential you have created.

![](./images/10.png)

If you are interested in using admin privileges, please use the following username and password
to login:

```
username: admin
password: admin
```

![](./images/9.png)

If you are interested in looking at the database in the backend, using the same admin credentials, you can access the admin portal by heading to:
http://127.0.0.1:8000/admin/

## Game collections

The "game collection" displays all the games belonging to a given collection.

A user can have multiple "game collections" within their game catalogue.

This functionality is designed to be expanded to allow different formats of games to be kept in collections, e.g boardgames, cardgames, videogames etc.

![](./images/1.png)

### Creating a game collection

Navigate to the "My Collection" page and press on "Create collection".

This will open a page with boxes for the user to fill-in related to the "game collection" that is to be added.

Update the boxes with the relevant information and click the "Submit" button at the bottom of the page.

![](./images/2.png)

### Update a game collection

Navigate to the "My Collection" page and choose the game collection you wish to update.

At the top of the game collection page you should click on "Update collection"

![](./images/3.png)

This will open a page with boxes for the user to fill-in related to the "game collection" that is to be added.

Update the boxes with the relevant information and click the "Submit" button at the bottom of the page.

![](./images/4.png)

### Delete a game collection

Navigate to the "My Collection" page and choose the game collection you wish to delete.

At the top of the game collection page you should click on "Delete collection"

You will be prompted for a confirmation of the deletion, if you are sure you wish to delete the game press the "Yes, delete." button.

![](./images/5.png)

## Games

### Adding a game

Navigate to the "My Collection" page and select the relevant "game collection" from the list.

All the games currently part of the collection in question will be listed.

To add a game click on the "Create Game" link at the top of the page.

This will open a page with boxes for the user to fill-in related to the game that is to be added.

Update the boxes with the relevant information and click the "Submit" button at the bottom of the page.

![](./images/6.png)

### Updating a game 

From the "Game collection" you will see all the games that are listed as being part of the collection.

To update the details of a particular game, click on the "Update Game" button  belonging to the game you wish to update.

![](./images/7.png)

This will open a page with boxes for the user to fill-in related to the game that is to be updated.

Make the desired changes to the relevant parts of the game (description, rules, category etc) and when satisfued, press the "Submit" button at the bottom of the page.

![](./images/6.png)

### Deleting a game

From the "Game collection" you will see all the games that are listed as being part of the collection.

To delete a particular game, click on the "Delete Game" button belonging to the game you wish to update.

![](./images/7.png)

You will be prompted for a confirmation of the deletion, if you are sure you wish to delete the game press the "Yes, delete." button.

![](./images/8.png)

### Searching a game
From each "Game collection", you have 3 search bars to use, one for each search category, Game Title, Game Category and Game Description.

![](./images/11.png)

Simply type in the search boxes you want to search up your game on, and the results will be filtered.
