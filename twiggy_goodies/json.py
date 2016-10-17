# coding: utf-8
from __future__ import absolute_import

import io
import os
import calendar
import json
import datetime
import six
import socket
import pytz

from twiggy import outputs
from twiggy_goodies.utils import force_text, get_log_level_str


NUMERIC_TYPES = (float,) + six.integer_types


class JsonOutput(outputs.Output):
    """Output from twiggy to JSON, useful for processing logs with logstash.
    """

    def __init__(self, filename=None, stream=None, source_host=None):
        assert stream or filename, 'Stream or filename should be given.'

        self.stream = stream
        self.filename = filename

        def serialize_msg(msg):
            return json.dumps(self.format(msg, source_host=source_host), ensure_ascii=False)

        super(JsonOutput, self).__init__(format=serialize_msg, close_atexit=True)

    def format(self, msg, source_host=None):
        if source_host is None:
            source_host = socket.gethostname()

        fields = msg.fields.copy()
        fields['level'] = get_log_level_str(fields['level'])
        timestamp = fields.pop('time')
        timestamp = datetime.datetime.utcfromtimestamp(calendar.timegm(timestamp))
        timestamp = timestamp.replace(tzinfo=pytz.utc)

        if msg.traceback:
            fields['exception'] = force_text(msg.traceback)

        for key, value in fields.items():
            if not isinstance(value, NUMERIC_TYPES):
                if isinstance(value, six.string_types):
                    fields[key] = force_text(value)
                else:
                    fields[key] = six.text_type(value)

        return self.get_log_entry(msg, timestamp, source_host, fields)

    @staticmethod
    def get_log_entry(msg, timestamp, source_host, fields):
        return {
            '@message': force_text(msg.text),
            '@timestamp': timestamp.isoformat(),
            '@source_host': source_host,
            '@fields': fields,
        }

    def _open(self):
        if self.filename:
            assert self.stream is None, 'You should not use arguments "stream" and "filename" together'

            dirname = os.path.dirname(self.filename)
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)

            self.stream = io.open(self.filename, 'a')

    def _close(self):
        if self.filename:
            # we only want to close the stream, if opened it ourself
            self.stream.close()

    def _write(self, msg):
        self.stream.write(force_text(msg + '\n'))
