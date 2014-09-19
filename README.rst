===============
django-crequest
===============

.. contents:: 

Overview
========
- **crequest** Take care of current request is silent way.
- **crequest** will bring you current request object of your django application from anywhere in your code.

Installing
==========

django-crequest is available at http://pypi.python.org/pypi/django-crequest
So it can be installed it by pip::

    $ python pip install django-crequest

Or you can grab the latest version tarball and ::

    $ python setup.py install

To enable ``django-crequest`` in your project

* Add ``crequest`` to *INSTALLED_APPS* in your **settings.py**
* Add ``crequest.middleware.CrequestMiddleware`` to ``MIDDLEWARE_CLASSES`` after the authentication and session middleware.


Supported Python versions
=========================

``django-crequest`` currently can be run on multiple python versions:

* Python 2 (2.7)
* Python 3 (3.2, 3.3, 3.4)
* PyPy


How to use
==========

First import the crequest's middleware::

    from crequest.middleware import CrequestMiddleware

Get the current ``request`` ;)::

    current_request = CrequestMiddleware.get_request()

Done.

Some info for some folks
========================

Set the current request in UnKnown situations::

     CrequestMiddleware.set_request(request)

Return *iam_request* if there is no current request::

    CrequestMiddleware.get_request(iam_request)

And finally delete::

    CrequestMiddleware.del_request()

The middleware automatically sets/deletes the current request for HTTP requests.
For other uses (management commands, scripts), you will need to do this yourself.

