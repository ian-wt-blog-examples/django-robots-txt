# django-robots-txt
A django project that serves a robots.txt file.

Check out my article [How To Add A robots.txt File In Django](https://ianwaldron.com/blog/how-to-add-a-robotstxt-file-in-django/) for more information.


```shell
python3 -m venv env
```

This operation might take a few seconds. Once installed, activate the virtual environment.

```shell
source env/bin/activate
```

Next, install the requirements (Django, etc.)

```shell
pip install -r requirements.txt
```

## Migrate Database

Migrating the database isn't strictly necessary. The development server will run without it but it will complain. So if you don't want the warning in the console, run the folling command.

```shell
python manage.py migrate
```

## Test robots.txt

Now start the application on a development server.

```shell
python manage.py runserver
```

Navigate to the robots.txt location running on the development server exposed at port 8000.

[robots.txt](http://127.0.0.1:8000/robots.txt)

## Switching Between Approaches

By default, the implemented approach is the view-only approach.

If you'd like to run the other, simply comment out the operational URL pattern and uncomment the other. This is in demo.urls.py.
