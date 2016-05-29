import six

from twiggy import levels


def force_str(text, encoding='utf-8'):
    if isinstance(text, six.binary_type):
        return text
    return text.encode(encoding)


def force_text(text, encoding='utf-8'):
    if isinstance(text, six.text_type):
        return text
    return text.decode(encoding)


def get_log_level_str(level):
    severity_names = {
        levels.CRITICAL: 'CRITICAL',
        levels.DEBUG:    'DEBUG',
        levels.ERROR:    'ERROR',
        levels.INFO:     'INFO',
        levels.WARNING:  'WARNING',
    }
    return severity_names[level]
