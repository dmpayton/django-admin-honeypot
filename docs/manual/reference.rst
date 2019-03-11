=========
Reference
=========

Settings
========

**ADMIN_HONEYPOT_EMAIL_ADMINS**

Default: ``True``

Used to determine whether or not to email site admins on login attempts. Set
to ``False`` to disable admin emails.

**ADMIN_HONEYPOT_REPORT_HPFEEDS**

Default: ``False``

Used to determine whether or not to send login attempts and other requests to an hpfeeds broker.

**ADMIN_HONEYPOT_LIMIT_DB**

Default: ``False``

Stores only necessary information in the local DB. This is useful if logging elsewhere (e.g. to hpfeeds) and local disk space is limited.


Signals
=======

:func:`admin_honeypot.signals.honeypot`

Sent on every login attempt with the following arguments:

:instance: The LoginAttempt object created
:request: The current request object
