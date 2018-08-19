'''
Server:
    Server network handler

'''

from collections import namedtuple
ClientInfo = namedtuple('ClientInfo', ['reader', 'writer'])

class Server(object):

    def __init__(self, *args, **kwargs):
        self.client_list = []
        pass

    def get_client_count(self):
        return len(self.client_list)

    def start(self):
        '''
        Open server connection
        '''
        pass

    def handle_open_connection(self, reader, writer):
        self.client_list.append(ClientInfo(reader, writer))
        self.handle_client_receive(reader.readline())
        pass
    def handle_client_receive(self, data):
        print(data)
        pass

