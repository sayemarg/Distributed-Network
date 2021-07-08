from server.cthread import ClientThread
from socket import socket, AF_INET, SOCK_STREAM


class Server:
    # Create TCP Socket With AF_INET Family And SOCK_STREAM (TCP) Type
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)

        # List Of Client's Server Port
        self.client_server_ports = {}

    # Bind Socket For Host And Port
    def bind(self, host, port):
        address = (host, port)
        self.server_socket.bind(address)

    # Listen For Client Connection
    def listen(self):
        self.server_socket.listen()
        print('Main Server Is Listening ...')

        while True:
            client_socket, address = self.server_socket.accept()
            print(f'New Connection To Main Server On {address}')

            client_thread = ClientThread(self, client_socket, address)
            client_thread.start()

    # Add Or Update Server Port To List
    def add_server_port(self, client_port, server_port):
        self.client_server_ports[client_port] = server_port

    # Remove Port From List
    def remove_server_port(self, client_port):
        del self.client_server_ports[client_port]

    # Return Port List Without Client Server Port
    def get_client_server_ports(self, client_port_filter=None):
        if client_port_filter:
            ports_list = self.client_server_ports.items()

            # Dictionary Key Should Not Be Client_port_filter
            ports_list = filter(lambda item: item[0] != client_port_filter, ports_list)
            ports_list = dict(ports_list)

            return list(ports_list.values())

        return list(self.client_server_ports.values())
