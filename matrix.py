from const import *


class Matrix:

    def __init__(self, line, column):

        self.__line = line
        self.__column = column
        self.__matrix = [[int(j) for j in range(line)] for i in range(column)]

    def print(self):

        for line in self.__matrix:
            print(*line, sep='')

    def draw(self, window, images):

        for j in range(self.__line):
            for i in range(self.__column):

                if self.__matrix[j][i] == 1:
                    window.blit(images['red_token.png'], (FIRST_POSITION_TOKEN_X, FIRST_POSITION_TOKEN_Y))

                if self.__matrix[j][i] == 2:
                    window.blit(images['yellow_token.png'], (FIRST_POSITION_TOKEN_X, FIRST_POSITION_TOKEN_Y))

