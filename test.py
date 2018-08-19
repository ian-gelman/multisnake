
from collections import namedtuple
import unittest
from unittest.mock import patch

from server import Server
from client import Client

ClientInfo = namedtuple('ClientInfo', ['reader', 'writer'])

class ServerTest(unittest.TestCase):

    def setUp(self):
        self.server = Server(host='0.0.0.0', port='6969')
        self.client = Client()

    def connect_client(self):
        self.server.start()
        self.client.connect(server_host='0.0.0.0', server_port='6969')

    def test_open_connection(self):
        prev_count = self.server.get_client_count()
        self.connect_client()
        count = self.server.get_client_count()
        self.assertGreater(prev_count, count)
        pass

    def test_handle_client_connect(self):
        pass

if __name__ == '__main__':
    unittest.main()
