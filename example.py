#!/usr/bin/env python

from twiggy_goodies.setup import setup_logging
from twiggy_goodies.threading import log

def some_function():
    log.info('inner function does not accept logger')
    log.info('but uses same field as caller')


setup_logging(None)

log.info('before request')

with log.fields(request_id='foo'):
    log.info('bar has happened')
    some_function()

log.info('after request, id gone')
