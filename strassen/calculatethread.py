from client.matrix import Matrix
from generic import HOST, MSG_TYPES
from methods import send_message, receive_message
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class CalculateThread(Thread):
    def __init__(self, port, matrix_01, matrix_02):
        super().__init__(daemon=True)

        self.port = port

        self.matrix_01 = matrix_01
        self.matrix_02 = matrix_02

        self.result_matrix = None

    # Connect To Port And Send Matrix To Calculate
    def run(self) -> None:
        try:
            calculate_socket = socket(AF_INET, SOCK_STREAM)
            calculate_socket.connect((HOST, self.port))

            send_message(calculate_socket, MSG_TYPES['MATRIX'], self.matrix_01.get_matrix())
            send_message(calculate_socket, MSG_TYPES['MATRIX'], self.matrix_02.get_matrix())

            data = receive_message(calculate_socket)

            if data['type'] == MSG_TYPES['MATRIX']:
                self.result_matrix = Matrix(data['message'])

            calculate_socket.close()

        except Exception:
            print("Some Thread Went Wrong! We Are Trying Again For Calculate...")

    # Get Thread Matrices When Thread Failed
    def get_matrices(self):
        return self.matrix_01, self.matrix_02

    # Get Result Matrix
    def get_result_matrix(self):
        return self.result_matrix
