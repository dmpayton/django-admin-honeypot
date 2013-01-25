=========
Reference
=========

Settings
========

**ADMIN_HONEYPOT_EMAIL_ADMINS**

Default: ``True``

Used to determine whether or not to email site admins on login attempts. Set
to ``False`` to disable admin emails.

Signals
=======

:func:`admin_honeypot.signals.honeypot`

Sent on every login attempt with the following arguments:

:instance: The LoginAttempt object created
:request: The current request object
