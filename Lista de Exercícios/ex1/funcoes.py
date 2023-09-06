espaco = " "
token = ["X", "O"]


def criarBoard():
  board = [
      [espaco,espaco,espaco,espaco],
      [espaco,espaco,espaco,espaco],
      [espaco,espaco,espaco,espaco],
      [espaco,espaco,espaco,espaco],
  ]
  return board

def printBoard(board):
  for i in range(4):
    print(" | ".join(board[i]))
    if(i<3):
      print("--------------") 

def getInputValido(mensagem):
  try:
    n = int(input(mensagem))
    if(n >= 1 and n <=4):
      return n - 1 
    else:
      print('Numero precisa estar entre 1 e 4')
      return getInputValido(mensagem)
  except:
    print("Numero não valido!")
    return getInputValido(mensagem)

def verificaMovimento(board, i, j):
  if board[i][j] == espaco:
    return True
  else:
    return False

def fazMovimento(board, i, j, jogador):
  board[i][j] = token[jogador]

def verificaGanhador(board):
  for i in range(4):
    if(board[i][0] == board[i][1] and board[i][1] and board[i][2] and board[2][i] == board[3][i] and board[i][0] != espaco):
      return board[i][0]

  #colunas
  for i in range(4):
    if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[0][i] != espaco):
      return board[0][i]

  #diagonal principal
  if(board[0][0] != espaco and board[0][0] == board [1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3]):
    return board[0][0]

  #diagonal secundaria
  if(board[0][3] != espaco and board[0][3] == board [1][2] and board[1][2] == board[2][1] and board[3][0]):
    return board[0][3]


  #talvez remova#####
  for i in range(4):
   for j in range (4):
    if board[i][j] == espaco:
      return False

  return "EMPATE"


