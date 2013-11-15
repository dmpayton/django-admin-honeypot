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

Once your requirements ae installed, the unit tests can be run with::

    $ python setup.py test

    ...

    ----------------------------------------------------------------------
    Ran 5 tests in 0.174s

    OK


For testing against different Python versions, we use `Tox`_::

    $ tox

    ...

    _______________ summary _______________
    py27: commands succeeded
    py33: commands succeeded
    congratulations :)


.. _Tox: http://tox.readthedocs.org/
