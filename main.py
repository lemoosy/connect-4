
from os import system



matrix = [[0 for j in range(7)] for k in range(6)]
game_off = False



def print_matrix():

	for line in matrix:
		print(*line, sep = '')

def out_of_dimension(line, column):

	return line < 0 or column < 0 or line >= 7 or column >= 6

def get_lines():

	return matrix

def get_columns():

	return list(map(list, zip(*matrix)))
		
def check_win():

	for line in get_lines() + get_columns():

		player1, player2 = 0, 0
		
		for case in line:

			if case == 0:
				player1, player2 = 0, 0

			if case == 1:
				player1 += 1

			if case == 2:
				player1 += 2

			if player1 == 4:
				return 1

			if player2 == 4:
				return 2

	return 0

def can_place_piece(column):

	return matrix[0][column] == 0

def place_piece(column, player):

	for line in range(5, -1, -1):

		if matrix[line][column] == 0:
			matrix[line][column] = player
			break



while not(game_off):

	for player in (1, 2):

		while True:

			system('cls')
			print_matrix()
			column = int(input('\nEnter a column player{} : '.format(player)))
	
			if not(out_of_dimension(0, column)):
				if can_place_piece(column):
					
					place_piece(column, player)
					game_off = check_win()
					break



input('player {} win !'.format(game_off))