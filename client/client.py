from .sthread import ServerThread
from strassen.strassen import Strassen
from generic import MSG_TYPES
from methods import send_message, receive_message
from socket import socket, AF_INET, SOCK_STREAM


class Client:
    # Create TCP Socket With AF_INET Family And SOCK_STREAM (TCP) Type
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)

        self.server_thread = ServerThread(self)

    # Connect To Main Server
    def connect(self, host, port):
        address = (host, port)
        self.client_socket.connect(address)

        # Run A Server For Each Client To Receive Matrix
        self.server_thread.start()

    # Close Connection Socket
    def close(self):
        self.client_socket.close()

    # To Get Server Port List From Main Server
    def get_client_server_ports(self):
        # Send Request For Port List
        send_message(self.client_socket, MSG_TYPES['REQ_LIST'], '')

        # Get Serialized Port List
        data = receive_message(self.client_socket)

        if data is None:
            return None

        elif data['type'] == MSG_TYPES['LIST']:
            return data['message']

    # Calculate Strassen For Given Matrices
    def calculate_strassen(self, matrix_01, matrix_02):
        strassen = Strassen(matrix_01, matrix_02, self.get_client_server_ports())
        result_matrix = strassen.calculate()

        return result_matrix
