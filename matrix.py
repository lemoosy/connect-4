
class Matrix:

    def __init__(self, line, column):

        self.__line = line
        self.__column = column
        self.__matrix = [[int(j) for j in range(line)] for i in range(column)]

    def print(self):

        for line in self.__matrix:
            print(*line, sep='')
