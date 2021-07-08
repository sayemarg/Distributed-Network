from .calculatethread import CalculateThread
from client.methods import add_matrix, subtract_matrix, multiply_matrix, split_matrix, concat_matrices
from random import choice, choices


class Strassen:
    # Constructor With Two Matrix
    def __init__(self, matrix_01, matrix_02, port_list=None):
        self.matrix_01 = matrix_01
        self.matrix_02 = matrix_02

        self.port_list = port_list

    def calculate(self):
        if self.port_list:
            # Send To Other Clients To Calculate
            return self.propagate_calculate()

        else:
            # Self Calculate If No Other Client Connected
            return self.self_calculate()

    def propagate_calculate(self):
        if self.matrix_01.get_dimension() == 2:
            return multiply_matrix(self.matrix_01, self.matrix_02)

        else:
            a_11, a_12, a_21, a_22 = split_matrix(self.matrix_01)
            b_11, b_12, b_21, b_22 = split_matrix(self.matrix_02)

            # Choose 7 Random Server To Connect
            port_list = choices(self.port_list, k=7)

            # Create CalculateThread For Each Strassen M Matrix
            thread_list = [CalculateThread(port_list[0], add_matrix(a_11, a_22), add_matrix(b_11, b_22)),
                           CalculateThread(port_list[1], add_matrix(a_21, a_22), b_11),
                           CalculateThread(port_list[2], a_11, subtract_matrix(b_12, b_22)),
                           CalculateThread(port_list[3], a_22, subtract_matrix(b_21, b_11)),
                           CalculateThread(port_list[4], add_matrix(a_11, a_12), b_22),
                           CalculateThread(port_list[5], subtract_matrix(a_21, a_11), add_matrix(b_11, b_12)),
                           CalculateThread(port_list[6], subtract_matrix(a_12, a_22), add_matrix(b_21, b_22))]

            # Result Of Threads For M1 To M7 Matrices
            m_list = []

            # Run Each Calculate Thread And Wait To Be Finished
            i = 0
            while i < len(thread_list):
                thread_list[i].start()

                # Wait To Thread Complete
                thread_list[i].join()

                result_matrix = thread_list[i].get_result_matrix()

                # ReCalculate If Result Is None
                if result_matrix is None:
                    random_port = choice(self.port_list)

                    thread_list[i] = CalculateThread(
                        random_port,
                        thread_list[i].matrix_01,
                        thread_list[i].matrix_02
                    )

                else:
                    m_list.append(result_matrix)

                    i = i + 1

            c_11 = add_matrix(subtract_matrix(add_matrix(m_list[0], m_list[3]), m_list[4]), m_list[6])
            c_12 = add_matrix(m_list[2], m_list[4])
            c_21 = add_matrix(m_list[1], m_list[3])
            c_22 = add_matrix(subtract_matrix(m_list[0], m_list[1]), add_matrix(m_list[2], m_list[5]))

            result = concat_matrices(c_11, c_12, c_21, c_22)

            return result

    def self_calculate(self):
        if self.matrix_01.get_dimension() == 2:
            return multiply_matrix(self.matrix_01, self.matrix_02)

        else:
            a_11, a_12, a_21, a_22 = split_matrix(self.matrix_01)
            b_11, b_12, b_21, b_22 = split_matrix(self.matrix_02)

            m_01 = Strassen(add_matrix(a_11, a_22), add_matrix(b_11, b_22)).self_calculate()
            m_02 = Strassen(add_matrix(a_21, a_22), b_11).self_calculate()
            m_03 = Strassen(a_11, subtract_matrix(b_12, b_22)).self_calculate()
            m_04 = Strassen(a_22, subtract_matrix(b_21, b_11)).self_calculate()
            m_05 = Strassen(add_matrix(a_11, a_12), b_22).self_calculate()
            m_06 = Strassen(subtract_matrix(a_21, a_11), add_matrix(b_11, b_12)).self_calculate()
            m_07 = Strassen(subtract_matrix(a_12, a_22), add_matrix(b_21, b_22)).self_calculate()

            c_11 = add_matrix(subtract_matrix(add_matrix(m_01, m_04), m_05), m_07)
            c_12 = add_matrix(m_03, m_05)
            c_21 = add_matrix(m_02, m_04)
            c_22 = add_matrix(subtract_matrix(m_01, m_02), add_matrix(m_03, m_06))

            result = concat_matrices(c_11, c_12, c_21, c_22)

            return result
