# AHS Freshman Debates
Judging App for Albany High School Freshman Renewal Debates.

# TODO
- Clean up admin debater import (hide CSV fields).
- Get Google authentication to work (Google + Sign In as OpenID and OpenAuth are being deprecated)
    - Integrate it to give permissions.
- Write tests
- Decide what should be done in admin versus in app.

# Requirements
- [Python](https://www.python.org/downloads/) 3.x

## Available Through PyPi
- [Django](https://www.djangoproject.com/) ([Django](https://pypi.python.org/pypi/Django/))
- Python Social Auth ([python-social-auth](https://pypi.python.org/pypi/python-social-auth/))
- Django Import / Export ([django-import-export](https://pypi.python.org/pypi/django-import-export))
    - Tablib ([tablib](https://pypi.python.org/pypi/tablib)) must currently be installed from Github
      (version on PyPi is 3 years old and does not support Python 3) using `pip install -e
      git+https://github.com/kennethreitz/tablib.git#egg=tablib`

# Setup
- ./manage.py syncdb (initialize database tables)
