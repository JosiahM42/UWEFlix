# UWE Assignment Year 3 | Enterprise Systems Development (ESD) | UWEFlix Cinema System | Group 8

## UWEFlix Django Web Application

To run the Django web application two nonstandard library must be installed, run 

```
pip install django-session-timeout
```

from the terminal. This is to allow for the sessions time out functions.
Then run

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

from the terminal to allow for the function required to use the Gmail API services that are intended to email users on successful booking.

From here the application can be run by running the following command from the terminal whilst in the UWEFLix Project Folder:
```
python manage.py runserver
```


Key Login Details Required:
New users are able to be signed up and login through the system, however a view examples have been provided for your convince.

Cinema Admin:
Username: Manager
Password: AdminMan

Account Admin:
Username: Accounts
Password: ????

Example Students/ Student Reps:

Username: movieLover42
Password: Testing42

Username: JebTheThird
password: Jeb123456789



## Design Work
Please see the UWEFLix design work folder to view the design work for this project, including users stories, non-requirement, and database design.




