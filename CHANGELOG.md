0.11.2 (2016-10-17)
===================

* All output of JsonOutput now encoded in utf-8 to be correctly written to file or terminal in presence of international characters.

0.11.1 (2016-10-17)
===================

* Fixed logging of longs in JsonOutput.

0.11.0 (2016-05-30)
===================

* Fixed issues with unicode encoding on Python 3 for `JsonOutput`.
* Now `JsonOutput` opens file using `io.open` instead of `os.open`
probably this could lead to some backward incompatibility.

0.10.0 (2016-05-26)
===================

* Fixed a way how `JsonOutput` serialized json. Now it uses standart `json`
library instead of `anyjson`, and works with unicode in tracebacks correctly.

0.9.0 (2016-05-26)
==================

* `JsonOutput` became more configurable and now format can be
changed by overloading `get_log_entry` method. Thanks to
the [Alexander Akhmetov](https://github.com/alexander-akhmetov).

0.8.0 (2016-05-25)
==================

* Now `filename` is optional for `JsonOutput`. And new parameter `stream` can be given.
For example, `stream=sys.stdout`.
* Also, `setup_logging` now uses `JsonOutput` with `stream=sys.stdout`, if
`filename` is `None` and `format='json'` (this is default). This makes
possible to output in JSON to stdout.

0.7.0 (2015-11-12)
==================

* Fixed json and syslog loggers for Python 3.5.
  They were unable to log tracebacks.

0.6.0 (2015-04-15)
==================

* Fixed errors with missing fieldsDict and addEmitters in `twiggy` >= 0.4.6 on python3.

0.5.0 (2014-09-23)
==================

* Fixed issue when twiggy's plain text broke on unicode field values.

0.4.1 (2014-08-20)
==================

* Django-rq's `job` decorator was fixed and now could be used
  with arguments, like the original one.

0.4.0 (2014-08-08)
==================

* Added new output `twiggy_goodies.logstash.LogstashOutput` which
  sends json encoded data via UDP to a logstash server.
* Fixed errors related to missing `severity_names` in `JsonOutput`,
  when `source_host` argument was specified.

0.3.1 (2014-08-06)
==================

* Fixed issue when json output returned local date instead of UTC.

0.3.0 (2014-08-06)
==================

* Now json serializer returns timestamp with explicit UTC timestamp.
  This probably could broke someone's log processing pipeline, so
  consider this release as backward incompatible.
* Also, now it depends on pytz package.

0.2.2 (2014-04-17)
==================

  * Fixed error in django logging middleware, caused by absent
    Content-Type header in DELETE responses from django-rest-framework.

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
