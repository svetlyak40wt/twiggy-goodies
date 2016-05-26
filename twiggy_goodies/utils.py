import six

from twiggy import levels


def force_str(text, encoding='utf-8'):
    if six.text_type(text):
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
