import six


def force_str(text, encoding='utf-8'):
    if six.text_type(text):
        return text
    return text.decode(encoding)
