from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move


@given(u'we have an empty tic-tac-toe board')
def empty_board(context):
    context.board = EMPTY_BOARD #make empty board
    context.winner = None #Set winner to none

@when(u'I play {token} on column {col} and row {row} on the board')
def play_X(context, token, col, row):
   row = int(row) - 1
   col = int(col) - 1
   context.board, context.winner = play(context.board, token, col, row)

@when(u'I ask the computer to do its best move for {token}')
def best_move(context,token):
    context.board, context.winner = play_best_move(context.board, token)


@then(u'the board has a {token} in column {col} and row {row} on the board')
def check(context,token,col,row):
   row = int(row) - 1
   col = int(col) - 1
   position_on_board = row * 3 + col
   assert context.board[position_on_board] == token

@then(u'{token} is the winner of the game')
def step_impl(context, token):
   if token == 'X' or token == 'O' or token == 'T':
      assert context.winner == token
   else:
      assert context.winner != 'X' and context.winner != 'O'