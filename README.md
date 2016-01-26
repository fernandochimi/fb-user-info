# fb-user-info
API to save user info from Facebook to your database

## How to use
* Create a virtualenv (I prefer use ``virtualenvwrapper``).
* Fork or clone this repo.
* Install ``requirments.txt`` with ``pip install -r requirments.txt``
* Before start, run ``python fb_user_info/manage.py migrate --settings=settings.dev``
* Run the project with ``python fb_user_info/manage.py runserver --settings=settings.dev``

## ``Makefile`` Tips
``Makefile`` was created to facilitate some commands.
* Execute ``make test`` to run the tests of project
* Execute ``make html`` to exhibit the cover of tests in browser
* Execute ``make clean`` to clean unecessary files of project
* Execute ``make doc`` to generate docs of the project

## ``requirements.txt``
* ``Django 1.8.8`` - Framework to support a admin site.
* ``Django Flat Theme`` - A nice Django theme.
* ``Restless`` - A python Rest microframework.
* ``Factory Boy`` - App to make mocks.
* ``Redis`` - Data structure store, used as database.
* ``Celery`` - Generate tasks to get more performance.
* ``Coverage`` - App to cover tests.
* ``Sphinx`` - Create docs for project.
* ``Requests`` - HTTP library.
