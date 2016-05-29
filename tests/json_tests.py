# coding: utf-8

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import io
import time
import six

from twiggy_goodies.json import JsonOutput
from twiggy.message import Message
from twiggy.levels import INFO


_default_fields = {
    'suppress_newlines': False,
    'trace': 'error',
    'style': 'percent',
}


def test_json_formatter_is_able_to_deal_with_unicode_fields():
    stream = io.StringIO()
    output = JsonOutput(stream=stream)
    message = Message(
        INFO,
        u'Некий текст',
        {
            'time': time.gmtime(),
            'blah': u'минор'
        },
        _default_fields,
        (),
        {},
    )

    output.output(message)
    result = stream.getvalue()
    assert isinstance(result, six.text_type)


def test_json_formatter_is_able_to_deal_with_utf8_fields():
    stream = io.StringIO()
    output = JsonOutput(stream=stream)
    message = Message(
        INFO,
        u'Некий текст'.encode('utf-8'),
        {
            'time': time.gmtime(),
            'blah': u'минор'.encode('utf-8')
        },
        _default_fields,
        (),
        {},
    )

    output.output(message)
    result = stream.getvalue()
    assert isinstance(result, six.text_type)
