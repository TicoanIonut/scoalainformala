import random

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def display_board():
	print(board[0] + '|' + board[1] + '|' + board[2] + '  1|2|3')
	print(board[3] + '|' + board[4] + '|' + board[5] + '  4|5|6')
	print(board[6] + '|' + board[7] + '|' + board[8] + '  7|8|9')


game_still_going = True
winner = None
players = ('x', '0')
current_player = random.choice(players)


def gameplay():
	display_board()
	replay()
	while game_still_going:
		handle_turn(current_player)
		check_if_game_over()
		flip_player()
	if winner == 'x' or winner == "o":
		print(f"{winner},won")
	elif winner is None:
		print('tie')


def handle_turn(player):
	print(player + "'s turn")
	if 'x' == player:
		poz_x(player)
	if '0' == player:
		poz_0(player)


def check_if_game_over():
	check_if_win()
	check_if_tie()


def check_if_win():
	global winner
	row_winner = check_rows()
	column_winner = check_columns()
	diagonal_winner = check_diagonal()
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None


def check_rows():
	global game_still_going
	row_1 = board[0] == board[1] == board[2] != '_'
	row_2 = board[3] == board[4] == board[5] != '_'
	row_3 = board[6] == board[7] == board[8] != '_'
	if row_1 or row_2 or row_3:
		game_still_going = False
	if row_1:
		return board[0]
	if row_2:
		return board[3]
	if row_3:
		return board[6]
	return


def check_columns():
	global game_still_going
	column_1 = board[0] == board[3] == board[6] != '_'
	column_2 = board[1] == board[4] == board[7] != '_'
	column_3 = board[2] == board[5] == board[8] != '_'
	if column_1 or column_2 or column_3:
		game_still_going = False
	if column_1:
		return board[0]
	if column_2:
		return board[1]
	if column_3:
		return board[2]
	return


def check_diagonal():
	global game_still_going
	diagonal_1 = board[0] == board[4] == board[8] != '_'
	diagonal_2 = board[6] == board[4] == board[2] != '_'
	if diagonal_1 or diagonal_2:
		game_still_going = False
	if diagonal_1:
		return board[0]
	if diagonal_2:
		return board[1]
	return


def check_if_tie():
	global game_still_going
	if '_' not in board:
		game_still_going = False
	return


def flip_player():
	global current_player
	if current_player == 'x':
		current_player = '0'
	elif current_player == '0':
		current_player = 'x'
	return


def poz_x(player):
	position = input('select position 1-9')
	valid = False
	while not valid:
		while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			position = input('invalid input, select position 1-9')
		position = int(position) - 1
		if board[position] == '_':
			valid = True
		else:
			print("can't go there, try again")
	board[position] = player
	display_board()


def poz_0(player):
	nums = '513792468'
	position = random.choice(nums)
	valid = False
	while not valid:
		while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			position = random.choice(nums)
		position = int(position) - 1
		if board[position] == '_':
			valid = True
		else:
			position = random.choice(nums)
			print("can't go there, try again")
	board[position] = player
	display_board()


def replay():
	while game_still_going is False:
		ask = input(f"{current_player}, Do you want to play again? y/n".lower())
		if ask == 'y':
			print(gameplay())
		else:
			print('Thank you for playing')
		break


gameplay()
