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

**ADMIN_HONEYPOT_ALLOW_TRACK_ADDRESS**

Default: ``False``

Used to allow track detail address from client.
Set to ``True`` to enable tracker.

**ADMIN_HONEYPOT_PATH_GEOIPV4_CITY**

Default: ``None``

Used to set path of ``GeoLiteCity.dat`` for ``IPV_4``.

**ADMIN_HONEYPOT_PATH_GEOIPV6_CITY**

Default: ``None``

Used to set path of ``GeoLiteCityv6.dat`` for ``IPV_6``.
