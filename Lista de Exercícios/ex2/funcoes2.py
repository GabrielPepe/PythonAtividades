espaco = " "
token = ["X", "O"]
board=[]


def criarBoard():
  liecol = int(input("Informe quantas linhas: "))
  for i in range(liecol):
    linha = []
    for j in range(liecol):
      linha.append(espaco)
    board.append(linha)

  return board

def printBoard(board):
  for i in range(len(board)):
    linha = board[i]
    #print(board)
    print(" | ".join(board[i]))
    if(i<len(board)):
      print("----"*len(board)) 

def getInputValido(mensagem):
  try:
    n = int(input(mensagem))
    if(n >= 1 and n <=len(board)):
      return n - 1 
    else:
      print(f'Numero precisa estar entre 1 e {len(board)}')
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
  #Linhas:
  for i in range(len(board)):
    cont = 0
    for x in range(1, len(board)):
        if(board[i][0] == board[i][x] and board[i][x] != espaco):
            cont+=1
    print(cont)
    print(len(board))
    if cont==len(board):
      print(f"Retornou {board[i][x]}")
      return board[i][x]

  #colunas
  for i in range(len(board)):
    cont = 0
    for x in range(1, len(board)):
        if(board[0][i] == board[x][i] and board[x][i] != espaco):
            cont+=1
    if cont==len(board):
      return board[x][i]
  """
    #Manual:

  for i in range(4):
    if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[0][i] != espaco):
      return board[0][i]
    """
  """
  #diagonal principal
  if(board[0][0] != espaco and board[0][0] == board [1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3]):
    return board[0][0]

  #diagonal secundaria
  if(board[0][3] != espaco and board[0][3] == board [1][2] and board[1][2] == board[2][1] and board[2][1] == board[3][0]):
    return board[0][3]
    """


  #talvez remova#####
  for i in range(len(board)):
   for j in range (len(board)):
    if board[i][j] == espaco:
      return False

  return "EMPATE"
  


