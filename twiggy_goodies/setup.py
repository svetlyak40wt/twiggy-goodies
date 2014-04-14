# coding: utf-8
from __future__ import absolute_import

import logging

from twiggy import addEmitters, outputs, levels, formats
from .json import JsonOutput
from .std_logging import RedirectLoggingHandler


def setup_logging(filename,
                  level=levels.DEBUG,
                  format='json',
                  redirect=True,
                  format_string=formats.line_format):

    if filename is None:
        output = outputs.StreamOutput(format=format_string)
    else:
        if format == 'json':
            output = JsonOutput(filename)
        else:
            output = outputs.FileOutput(filename, format=format_string)

    addEmitters(('emitter', level, None, output))

    if redirect:
        # redirect standart logging to twiggy
        del logging.root.handlers[:]
        logging.root.addHandler(RedirectLoggingHandler())
