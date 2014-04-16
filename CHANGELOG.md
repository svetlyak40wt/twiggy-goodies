0.2.1 (2014-04-16)
==================

  * Fixed error when JsonOutput should write log into the current directory
    but tries to create it first.

0.2.0 (2014-04-16)
==================

This version makes futher steps to stiched log messages in
Django projects. It introduces several improvements:

  * A middleware `twiggy_goodies.django.LogMiddleware`, which groups all messages,
    logged within same http request-response cycle.
  * A mixin for management commands `twiggy_goodies.django.LogMixin`, which does
    same thing but for management commands.
  * A decorator `twiggy_goodies.django_rq.job` which stitches messages within
    single `python-rq's` job.

Logging configuration of `django-rq` and `python-rq` is non-trivial, so may be
I should write a separate documentation page with example.

0.1.0 (2014-04-14)
==================

  * Initial version with thread-local loggers stack
    and two context managers `fields` and `name`.
  * SysLogOutput.
  * JsonOutput.
