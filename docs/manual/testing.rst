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

Once your requirements are installed, the unit tests can be run with::

    $ py.test tests/ --cov admin_honeypot --cov-report term-missing --pep8 admin_honeypot

    ...

    =============== 5 passed, 12 skipped in 0.46 seconds ===============


For testing against different Python versions, we use `Tox`_. Please be aware
that this only tests against the latest Django release.

::

    $ tox

    ...

    _______________ summary _______________
    django-2x: commands succeeded
    django-3x: commands succeeded
    congratulations :)


.. _Tox: http://tox.readthedocs.org/
