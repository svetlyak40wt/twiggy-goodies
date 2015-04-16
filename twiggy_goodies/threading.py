# coding: utf-8
from __future__ import absolute_import

import threading
import contextlib

from collections import deque
from twiggy import log as _twiggy_log


class ThreadAwareLogger(object):
    """This object actually keeps a stack
    of loggers, local to a thread. And when
    somebody tries to log something, it
    simply call a topmost logger.

    Using this with context manager methods
    allows you to bind some data to log messages
    without passing logger object from one
    method or function to another.
    """

    thread_data = threading.local()

    def __init__(self, logger):
        self.thread_data.loggers_stack = deque([logger])

    def get_top_logger(self):
        stack = getattr(self.thread_data, 'loggers_stack', deque())
        if not stack:
            # if there isn't any stack then create it and add a root logger to it
            stack.append(_twiggy_log)
            self.thread_data.loggers_stack = stack

        return stack[-1]

    def __getattr__(self, name):
        _logger = self.get_top_logger()
        value = getattr(_logger, name)
        return value

    @contextlib.contextmanager
    def fields(self, **kwargs):
        new_logger = self.get_top_logger().fields_dict(kwargs)
        self.thread_data.loggers_stack.append(new_logger)
        yield
        self.thread_data.loggers_stack.pop()

    @contextlib.contextmanager
    def name_and_fields(self, name, **kwargs):
        new_logger = self.get_top_logger().name(name).fields_dict(kwargs)
        self.thread_data.loggers_stack.append(new_logger)
        yield
        self.thread_data.loggers_stack.pop()

log = ThreadAwareLogger(_twiggy_log)
