
def display_board(board):
  print(f' {board[0]} | {board[1]} | {board[2]} ')
  print('-----------')
  print(f' {board[3]} | {board[4]} | {board[5]} ')
  print('-----------')
  print(f' {board[6]} | {board[7]} | {board[8]} ')


def check_win(board, player):
  if (board[0] == player and board[1] == player and board[2] == player) or \
     (board[3] == player and board[4] == player and board[5] == player) or \
     (board[6] == player and board[7] == player and board[8] == player) or \
     (board[0] == player and board[3] == player and board[6] == player) or \
     (board[1] == player and board[4] == player and board[7] == player) or \
     (board[2] == player and board[5] == player and board[8] == player) or \
     (board[0] == player and board[4] == player and board[8] == player) or \
     (board[2] == player and board[4] == player and board[6] == player):
       return True
  return False


def check_full(board):
  for square in board:
    if square == ' ':
      return False
  return True


board = [' ' for _ in range(9)]  
player = 'X'  
while True:
  
  display_board(board)
  
 
  move = int(input(f'{player}, enter your move (0-8): '))
  while board[move] != ' ':
    print('That square is already taken!')
    move = int(input(f'{player}, enter your move (0-8): '))
  

  board[move] = player
  

  if check_win(board, player):
    display_board(board)
    print(f'{player} has won!')
    break
  

  if check_full(board):
    display_board(board)
    print('The game is a draw!')
    break
  

  if player == 'X':
    player = 'O'
  else:
    player = 'X'
