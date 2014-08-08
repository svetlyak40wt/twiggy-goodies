import socket
from .json import JsonOutput


class LogstashOutput(JsonOutput):
    """Output from twiggy to Logstash's UDP port
    All messages are serialized into json.
    """
    def __init__(self, host, port, source_host=None):
       super(LogstashOutput, self).__init__(None, source_host=source_host)
       del self.filename
       self.host = host
       self.port = port

    def _open(self):
        # we don't need to create connection for UDP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _close (self):
        self.socket.close()

    def _write(self, msg):
        self.socket.sendto(msg, (self.host, self.port))
