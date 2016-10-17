# coding: utf-8

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import io
import time
import six
import sys

from twiggy_goodies.json import JsonOutput
from twiggy.message import Message
from twiggy.levels import INFO


_default_fields = {
    'suppress_newlines': False,
    'trace': 'error',
    'style': 'percent',
}


def test_json_formatter_is_able_to_deal_with_unicode_fields():
    # logger usually writes it's output to some file and should
    # encode data into some binary encoding, for example utf-8
    stream = io.BytesIO()
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
    assert isinstance(result, six.binary_type)


def test_json_formatter_is_able_to_deal_with_utf8_fields():
    stream = io.BytesIO()
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
    assert isinstance(result, six.binary_type)


def test_json_formatter_does_not_dump_long_as_string():
    # https://github.com/svetlyak40wt/twiggy-goodies/issues/3
    if sys.version_info.major == 2:
        # this test makes sense only for python 2.x
        # because there is no separation between integer and long
        # in python 3

        stream = io.BytesIO()
        output = JsonOutput(stream=stream)
        message = Message(
            INFO,
            u'Какой-то текст сообщения',
            {
                'time': time.gmtime(),
                'request_id': long(1234),
            },
            _default_fields,
            (),
            {},
        )

        output.output(message)
        result = stream.getvalue()
        assert '"request_id": 1234' in result.decode('utf-8')
