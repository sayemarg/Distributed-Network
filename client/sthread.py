from .scthread import ServerClientThread
from generic import HOST, MSG_TYPES
from methods import send_message
from random import randint
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class ServerThread(Thread):
    def __init__(self, main_client):
        # daemon=True For Stop Thread In Close
        super().__init__(daemon=True)

        self.server_socket = socket(AF_INET, SOCK_STREAM)

        self.main_client = main_client

    # Create Server For Each Client With Random Port
    def run(self) -> None:
        while True:
            try:
                port = randint(40000, 60000)

                address = (HOST, port)
                self.server_socket.bind(address)

                send_message(self.main_client.client_socket, MSG_TYPES['MY_PORT'], port)
                break

            except Exception:
                pass

        self.listen()

    # Listen For Connection Request From Other Client
    def listen(self):
        self.server_socket.listen()

        while True:
            client_socket, address = self.server_socket.accept()

            server_client_thread = ServerClientThread(self.main_client, client_socket, address)
            server_client_thread.start()
