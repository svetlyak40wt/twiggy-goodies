# -*- coding: utf-8 -*-
from __future__ import absolute_import

import uuid

from twiggy_goodies.threading import log


class LogMixin(object):
    def execute(self, *args, **options):
        self.command_name = self.__class__.__module__.rsplit('.')[-1]

        fields = dict(args=', '.join(args), uuid=str(uuid.uuid4()))
        fields.update((key, value)
                      for key, value in options.items()
                      if value is not None)

        # For convenience to not make
        # from twiggy_goodies.threading import log
        # in each command
        self.logger = log

        with log.name_and_fields('command.' + self.command_name,
                                           **fields):
            log.info('Running command')
            try:
                return super(LogMixin, self).execute(*args, **options)
            except Exception:
                log.trace().error('Unhandled exception')
                raise


class LogMiddleware(object):
    def process_request(self, request):
        request.uuid = str(uuid.uuid4())
        request._logger_ctx = log.name_and_fields('django.http',
                                                  uuid=request.uuid,
                                                  method=request.method,
                                                  path=request.path)
        request._logger_ctx.__enter__()
        log.info('Request accepted')

    def process_response(self, request, response):
        code = response.status_code

        fields = dict(status_code=code)
        if 'content-type' in response:
            fields['content_type'] = response['content-type']
            
        with log.fields(**fields):
            method = log.error if code >= 500 else log.info
            method('Request processed')

        request._logger_ctx.__exit__(None, None, None)

        response['X-Request-Id'] = request.uuid
        return response
