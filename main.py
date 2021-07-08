from client.client import Client
from client.methods import get_matrix_from_user, read_matrix_from_file
from generic import HOST, PORT
from methods import print_line, get_int
from server.server import Server


# For Run Main Server At First
def run_main_server():
    main_server = Server()
    main_server.bind(HOST, PORT)
    main_server.listen()


# Interact With User In CLI
def run_user_client():
    user_client = Client()
    user_client.connect(HOST, PORT)

    while True:
        print_line()
        choice = get_int('What You Want? (1- Enter Matrices), (2- Read Matrices From File), (3- Close And Exit)')

        if choice == 1:
            print_line()
            matrix_01 = get_matrix_from_user('Matrix 01')
            print_line()
            matrix_02 = get_matrix_from_user('Matrix 02')

            result_matrix = user_client.calculate_strassen(matrix_01, matrix_02)
            print(result_matrix)

        elif choice == 2:
            matrix_01, matrix_02 = read_matrix_from_file()

            result_matrix = user_client.calculate_strassen(matrix_01, matrix_02)
            print(result_matrix)

        elif choice == 3:
            user_client.close()
            break

        else:
            print('Wrong Choice! Try Again.')


# Main Function To Run
def main():
    choice = get_int('What You Want To Run? (1- Main Server), (2- Client), (Other- Close)')

    if choice == 1:
        run_main_server()

    elif choice == 2:
        run_user_client()


# Run Main And Handle KeyInterrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
