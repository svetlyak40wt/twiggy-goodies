# coding: utf-8
from __future__ import absolute_import

import logging
import re

from twiggy import levels
from .threading import log


class RedirectLoggingHandler(logging.Handler):
    """A handler for the stdlib's logging system that redirects
    transparently to twiggy.
    """

    def __init__(self):
        logging.Handler.__init__(self)

    def convert_level(self, record):
        """Converts a logging level into a logbook level."""
        level = record.levelno
        if level >= logging.CRITICAL:
            return levels.CRITICAL
        if level >= logging.ERROR:
            return levels.ERROR
        if level >= logging.WARNING:
            return levels.WARNING
        if level >= logging.INFO:
            return levels.INFO
        return levels.DEBUG

    def find_extra(self, record):
        """Tries to find custom data from the old logging record.  The
        return value is a dictionary that is merged with the log record
        extra dictionaries.
        """
        rv = vars(record).copy()
        for key in ('name', 'msg', 'args', 'levelname', 'levelno',
                    'pathname', 'filename', 'module', 'exc_info',
                    'exc_text', 'lineno', 'funcName', 'created',
                    'msecs', 'relativeCreated', 'thread', 'threadName',
                    'processName', 'process'):
            rv.pop(key, None)
        return rv

    def emit(self, record):
        logger = log.get_top_logger()

        logger = logger.name(record.name) \
           .fields_dict(self.find_extra(record)) \

        if record.exc_info:
            logger = logger.trace(record.exc_info)

        message = record.getMessage()
        # These brakets should be escaped because twiggy tries to
        # insert an unexisted keyword arguments there :(
        message = re.sub(r'({|})', r'\1\1', message)
        logger._emit(self.convert_level(record), message, (), {})
