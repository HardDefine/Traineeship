from tictactoe import EMPTY_BOARD, play, get_printable_board, play_best_move

board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
winner = None # set the winner to None

board, winner = play(board, 'X', 2, 2) # take middle position
board, winner = play_best_move(board, 'O') # winner == None
print(get_printable_board(board))
print('------------------------------')
board, winner = play(board, 'X', 2, 0) # winner == None
board, winner = play_best_move(board, 'O') # winner == None
print(get_printable_board(board))
print('------------------------------')
board, winner = play(board, 'X', 0, 1) # winner == None
board, winner = play_best_move(board, 'O') # winner == None
print(get_printable_board(board))
board, winner = play(board, 'X', 1, 1) # winner == None
board, winner = play_best_move(board, 'O') # winner == None
print(get_printable_board(board))
board, winner = play(board, 'X', 1, 2) # winner == None
print(winner)