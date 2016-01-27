# fb-user-info

![alt text](https://cdn1.iconfinder.com/data/icons/logotypes/32/square-facebook-128.png "Facebook")

API to save user information from Facebook to your database.

## How to use
* Create a virtualenv (``virtualenvwrapper`` is recomended).
* Fork or clone this repo.
* Install ``requirments.txt`` with ``pip install -r requirments.txt``
* Before start, run ``python fb_user_info/manage.py migrate --settings=settings.dev``
* Create a superuser with ``python fb_user_info/manage.py createsuperuser --settings=settings.dev`` to access admin page (``http://localhost:8000/admin``)
* Access the ``base.py`` on ``fb_user_info/settings/`` directory and change the access token in ``FACEBOOK_TOKEN`` (You get the access token in ``https://developers.facebook.com/tools/explorer``)
* In another terminal, run ``redis-server`` to activate the service
* In another terminal, enter on ``fb_user_info`` (with underscores) and run ``celery worker -A settings -l INFO`` to activate ``Celery`` service
* Run the project with ``python fb_user_info/manage.py runserver --settings=settings.dev``

## ``Makefile`` Tips
``Makefile`` was created to facilitate some commands.
* Execute ``make doc`` to generate docs of the project (Note: uncomment the line 4 ``open docs/_build/html/index.html`` if necessary, and comment the line below).
* Execute ``make test`` to run the tests of project.
* Execute ``make html`` to exhibit the cover of tests in browser (Note: uncomment the line 14 ``open htmlcov/index.html`` if necessary, and comment the line below).
* Execute ``make clean`` to clean unecessary files of project.

## ``requirements.txt``
* ``Django 1.8.8`` - A Python Framework to support the project.
* ``Django Flat Theme`` - A nice Django theme.
* ``Restless`` - A python Rest microframework.
* ``Factory Boy`` - App to make mocks.
* ``Redis`` - Data structure store, used as database.
* ``Celery`` - Generate tasks to get more performance.
* ``Coverage`` - App to cover tests.
* ``Sphinx`` - Create docs for project.
* ``Sphinx RTD Theme`` - Theme for docs.
* ``Requests`` - HTTP library.
