from .matrix import Matrix
from generic import MSG_TYPES
from methods import send_message, receive_message
from threading import Thread


class ServerClientThread(Thread):
    def __init__(self, main_client, client_socket, address):
        super().__init__(daemon=True)

        self.main_client = main_client

        self.client_socket = client_socket
        self.address = address

        # To Keep Received Matrices
        self.matrix_list = []

    # Override Thread Run Function
    def run(self) -> None:
        while True:
            data = receive_message(self.client_socket)

            # Connection Close Message
            if data is None:
                self.client_socket.close()
                break

            # Get Matrix From Other Side Client
            elif data['type'] == MSG_TYPES['MATRIX']:
                matrix = Matrix(data['message'])
                self.matrix_list.append(matrix)

                # When 2 Matrix Received, Main Client Should Calculate Multiplication
                if len(self.matrix_list) == 2:
                    result_matrix = self.main_client.calculate_strassen(self.matrix_list[0], self.matrix_list[1])

                    # Send Result To Client That Requested Calculation
                    send_message(self.client_socket, MSG_TYPES['MATRIX'], result_matrix.get_matrix())

                    self.matrix_list.clear()
