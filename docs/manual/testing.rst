Testing
=======

Continuous integration provided by `Travis CI`_.

**master** (latest stable):
    |travis-ci-master|_
**develop** (bleeding edge):
    |travis-ci-develop|_

.. _Travis CI: https://travis-ci.org/

.. |travis-ci-master| image:: https://secure.travis-ci.org/dmpayton/django-admin-honeypot.png
.. _travis-ci-master: http://travis-ci.org/dmpayton/django-admin-honeypot

.. |travis-ci-develop| image:: https://secure.travis-ci.org/dmpayton/django-admin-honeypot.png?branch=develop
.. _travis-ci-develop: http://travis-ci.org/dmpayton/django-admin-honeypot

Test requirements
-----------------

See *requirements.txt*:

.. literalinclude:: ../../requirements.txt

Running the tests
-----------------

::

    $ python setup.py test
