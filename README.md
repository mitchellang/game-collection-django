# README

## Starting the application

Make sure you have django installed
This prototype was tested using anaconda supplied Python; 3.7.7

To install django

```
conda install -c anaconda django
```

Follow prompts until successfuelly installed along with any dependacies.

To start the django server move into the application directory containing the "manage.py" file

Here, run 

```
python manage.py runserver
```

This will prompt you with:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 10, 2020 - 12:54:41
Django version 3.0.3, using settings 'game_management_system.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open the application in a web-browser by pasting the hyperlink http://127.0.0.1:8000/

## Creating a login

The application requires each user to create a login.

The other pages will not render until this has been completed.

If you have not logged in before you should click on the "Lost password?" link, where you can sign up.

## Game collections

The game collection displays all the games belonging to a given collection.

This functionality is designed to be expanded to allow different formats of games to be kept in collections, e.g boardgames, cardgames, videogames etc.

### Adding a game collection

### Updating a game collection

### Deleting a game collection

## Managing your games within your game collection

### Adding a game

### Updating a game

### Deleting a game


