# coding: utf-8
from __future__ import absolute_import

import syslog
from twiggy import outputs, levels, formats
from twiggy_goodies.utils import force_str


class SysLogOutput(outputs.Output):
    """Output from twiggy into SysLog.
    """
    # from <linux/sys/syslog.h>:
    LOG_CRIT      = 2       #  critical conditions
    LOG_ERR       = 3       #  error conditions
    LOG_WARNING   = 4       #  warning conditions
    LOG_INFO      = 6       #  informational
    LOG_DEBUG     = 7       #  debug-level messages


    priority_names = {
        levels.CRITICAL: LOG_CRIT,
        levels.DEBUG:    LOG_DEBUG,
        levels.ERROR:    LOG_ERR,
        levels.INFO:     LOG_INFO,
        levels.WARNING:  LOG_WARNING,
    }

    def __init__(self, ident=('some-project', 'with-suffix')):
        self.ident = u'/'.join(filter(None, ident))


        def format(msg):
            priority = self.priority_names.get(msg.level,
                                               self.LOG_WARNING)

            fields = formats.line_conversion.convert(msg.fields)
            text = fields + u':' + msg.text
            if msg.traceback:
                text += u'\n' + force_str(msg.traceback)

            text = text.encode('utf-8')
            text = text.encode('string_escape')
            return priority, text

        super(SysLogOutput, self).__init__(format=format, close_atexit=True)


    def _open(self):
        syslog.openlog(self.ident.encode('utf-8'))

    def _close (self):
        syslog.closelog()

    def _write(self, msg):
        priority, msg = msg
        syslog.syslog(priority, msg)
