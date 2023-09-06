from funcoes import *

jogador = 0

board = criarBoard()
ganhador = verificaGanhador(board)
while(not ganhador): 
  printBoard(board)
  i = getInputValido("Digite a linha: ")
  j = getInputValido("Digite a coluna: ")

  if(verificaMovimento(board, i, j)):
    fazMovimento(board, i ,j, jogador)
    jogador = (jogador + 1)%2
  else:
    print("A posicao informada ja esta ocupada")
  ganhador = verificaGanhador(board)

print(ganhador)