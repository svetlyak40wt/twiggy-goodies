from __future__ import absolute_import

import uuid

from functools import wraps
from .threading import log
from django_rq import job as _job


def job(func_or_queue, connection=None, *args, **kwargs):
    """This decorator does all what django_rq's one, plus
    it group all logged messages using uuid and sets
    job_name field as well."""
    decorated_func = _job(func_or_queue, connection=connection, *args, **kwargs)

    if callable(func_or_queue):
        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            with log.fields(uuid=uuid.uuid4(),
                            job_name=decorated_func.__name__):
                return decorated_func(*args, **kwargs)
        return wrapper
    else:
        def decorator(func):
            @decorated_func
            @wraps(func)
            def wrapper(*args, **kwargs):
                with log.fields(uuid=uuid.uuid4(),
                                job_name=func.__name__):
                    return func(*args, **kwargs)
            return wrapper
        return decorator
