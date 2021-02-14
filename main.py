







matrix = [[0 for j in range(7)] for k in range(6)]


matrix[0][2] = 1
matrix[0][3] = 1
matrix[0][4] = 1




def print_matrix():

	for line in matrix:
		print(*line, sep = '')

def get_lines():

	return matrix

def get_columns():

	return list(map(list, zip(*matrix)))
		







input()