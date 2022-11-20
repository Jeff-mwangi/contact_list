# Contacts List Application 👨‍💼
## contacts-list Template
contacts-list app template

![Optional Text](/static/img/complete_contact_list.png)

## Description
This is a simple contacts list application that allows you to add, edit, search and delete contacts. It is built on Django framework and uses a Postgres database to store the contacts.

## Setting up and Running the application
1. Clone the repository using the following command
```
git clone
```
2. Create a virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Create a Postgres database and add the credentials to the .env file
5. Run the migrations
```
python manage.py migrate
```
6. Run the application
```
python manage.py runserver
```

Congrats! The application is now running 🥳