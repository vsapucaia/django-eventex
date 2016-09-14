# Welcome to the Django learning course.

This is a Django application to serve a website

[![Build Status](https://travis-ci.org/vsapucaia/django-eventex.svg?branch=master)](https://travis-ci.org/vsapucaia/django-eventex) [![Code Health](https://landscape.io/github/vsapucaia/django-eventex/master/landscape.svg?style=flat)](https://landscape.io/github/vsapucaia/django-eventex/master)

## How to develop

1. Clone repository
2. Create a new python 3.5 virtualenv
3. Activate virtualenv
4. Install requirements
5. Configure the instance with the .env
6. Run tests

```console
git clone git@github.com:vsapucaia/django-eventex.git
cd wttd
python -venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```


## How to deploy

1. Create a new heroku instance
2. Send configs to heroku
3. Define a better and safe SECRET_KEY
4. Set DEBUG=False
5. Configure e-mail service
6. push repo to heroku

```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure e-mail
git push heroku master --force
```
