# LAB - Class 34

## Project: Cookie Stand API

[deployed api on Vercel](https://cookie-stand-api-dlt.vercel.app/)

### Author: Cody De La Torre

### Links and Resources

* Django Rest Framework
* PostgreSQL
* ElephantSQL
* [Code Fellows API QuickStart](https://github.com/codefellows/python-401-api-quickstart)

### Setup

* Clone down repo to local machine.
* Create and activate a virtual environment.
* Run `pip install -r requirements.txt`.
* Add `.env` file in the `project` directory with follpwing info:
* You won't able to access the database information without logging in. In the URL, add `/admin` and log in with:
  * Username: `admin`
  * Password: `uncommon`
* You can also go `/api/v1/stand/` to access, create, update, and delete homes in the database.

### Tests

* ***When testing, make sure to NOT use PostgreSQL. COmment out the `.env` DATABASE fields to run tests***
* Run `python manage.py test` to run tests.
* ***Remember to un-comment out the DATABASE fields in the `.env` file when done with testing***.
