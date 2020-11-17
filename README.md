# DRF API and CSV import.
##### Simple API with CSV import in admin panel.

## Requirements

* Python 3.8.6
* Django 3.1.3
* Django REST framework 3.12.2
* django-filter 2.4.0


# Installation
##### Git clone this repository to your your environment:

    git clone https://github.com/KovalivSviatoslav/DRF_admin_csv_import.git

##### Move into your the cloned repository with "cd" command. For example:

    cd src

##### Install packages using `pip`:

    pip install -r requirements.txt

##### Run following commands at first project run:

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser

##### Next step is running your server. For that use:

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
