# DRF API and CSV import.
##### Simple API with CSV import in admin panel.

## Requirements

* Python 3.8.6
* Django 3.1.3
* Django REST framework 3.12.2
* django-filter 2.4.0


# Installation
Git clone this repository to your PC:

    git clone https://github.com/KovalivSviatoslav/DRF_admin_csv_import.git

Cd into your the cloned repository as such:

    cd src

Install using `pip`...

    pip install -r requirements.txt



###### Startup up a this project like so..

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

# API

URL Style | HTTP Method | Action
------------------|-------------|-----------------
/customers/ | GET | returns a list of customers
/customers/ | POST | creates a customer
/customers/{id}/ | GET | retrieve a customer
/customers/{id}/ | PUT | update a customer
/customers/{id}/ | PATCH | partial customer update
/customers/{id}/ | DELETE | remove a customer
/customer/?created_at={yyyy-mm-dd} | GET | customer filter by creation date

# END