=========
Reference
=========

Settings
========

**ADMIN_HONEYPOT_EMAIL_ADMINS**

Default: ``True``

Used to determine whether or not to email site admins on login attempts. Set
to ``False`` to disable admin emails.

**ADMIN_HONEYPOT_RECORD_PASSWORD**

Default: ``False``

Used to determine whether or not passwords entered will be recorded. If the honeypot is installed a working site and people have access to the database, then this is a bad idea. Otherwise, set to ``True`` to collect passwords.

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
