# My first Online course WEB/APP project
## steps 
### Be sure to have the following installed on your computer
- Python latest version which pip get installed with it automatically run this to check `Python -V`
- Django run this to check `python -m django –version` if not installed install it using pip `pip install django`
- PostgreSQL and have it connected 
### Install the required package
- Django needs an adpter called `Psycopg2` as an interface to work with PostgraSQL you can install it using this command 
`python -m pip install Psycopg2-binary`
- Install the required package for this project run `python -m pip install -U -r requirements.txt`
### Activate the Model for the App
- You need to perform migration for first time running to create nessesary tables run `python manage.py makemigrations`
- Run migration to activate model for the app run `python manage.py migrate`
- Run `python manage.py runserver` to check the online course app

Then you gonna see the Online course loads up site load up..
## Update the App with your Data 
It is an online course App you you need to be a superuser by creating an admin account so you can perform some CRUD operation on the site and see your course App

## Update the app data
- create an admin user `python manage.py createsuperuser` register your account, your username and password you should see superuser created successfully
- Run `python manage.py runserver` and navigate to your localhost admin directory on the browser **yourlocalhost/admin** to loging and perform some **CRUD** Operation on the App
- To Add some Course to the App after login-in the admin dashboard navigate to course and fill the data to be updated 

## Contributing
1. Fork the Repo
2. Make changes
3. Send your pull request for review..

## Show Love 💓

Show Love by giving the Repo a star...😇

# New Link at [Tolu John](https://tolujohnport.netlify.app/)
