from generic import MSG_TYPES
from methods import send_message, receive_message
from threading import Thread


class ClientThread(Thread):
    def __init__(self, server, client_socket, address):
        super().__init__(daemon=True)

        self.server = server

        self.client_socket = client_socket
        self.address = address

    # Override Thread Run Function
    def run(self) -> None:
        while True:
            data = receive_message(self.client_socket)

            if data is None:
                self.client_socket.close()
                self.server.remove_server_port(self.address[1])
                print(f"Connection On Address {self.address} Closed By User.")
                break

            elif data['type'] == MSG_TYPES['MY_PORT']:
                self.server.add_server_port(self.address[1], data['message'])
                print(f"Server On Port {data['message']} Added To List For Client On Port {self.address[1]}")

            elif data['type'] == MSG_TYPES['REQ_LIST']:
                client_server_ports = self.server.get_client_server_ports(self.address[1])

                send_message(self.client_socket, MSG_TYPES['LIST'], client_server_ports)
