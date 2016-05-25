# coding: utf-8
from __future__ import absolute_import

import sys
import logging

from twiggy import add_emitters, outputs, levels, formats
from .json import JsonOutput
from .std_logging import RedirectLoggingHandler


_default_line_formatter = formats.line_format
# twiggy tries to convert all values to string,
# but when value is unicode this leads to UnicodeEncodeError
# so it is better to make genericValue a smarter

def smart_str(value):
    if isinstance(value, unicode):
        return value.encode('utf-8')
    elif isinstance(value, str):
        return value
    return str(value)

_default_line_formatter.conversion.genericValue = smart_str


def setup_logging(filename,
                  level=levels.DEBUG,
                  format='json',
                  redirect=True,
                  format_string=_default_line_formatter):

    if filename is None:
        if format == 'json':
            args = {}
            if filename:
                args['filename'] = filename
            else:
                args['stream'] = sys.stdout

            output = JsonOutput(**args)
        else:
            output = outputs.StreamOutput(format=format_string)
    else:
        if format == 'json':
            output = JsonOutput(filename)
        else:
            output = outputs.FileOutput(filename, format=format_string)

    add_emitters(('emitter', level, None, output))

    if redirect:
        # redirect standart logging to twiggy
        del logging.root.handlers[:]
        logging.root.level = 0 # to pass all messages to redirect handler
        logging.root.addHandler(RedirectLoggingHandler())
