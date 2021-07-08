class Matrix:
    # Constructor
    def __init__(self, matrix=None):
        self.matrix = matrix

    # Set And Get 2 Dimensional Array For Matrix
    def set_matrix(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    # Get Dimensions Of Matrix
    def get_dimension(self):
        return len(self.matrix)

    def __str__(self):
        return str(self.matrix)
