from funcoes import *
from random import *

jogador = 0

board = criarBoard()
ganhador = verificaGanhador(board)
while(not ganhador): 
  printBoard(board)
  i = getInputValido("Digite a linha: ")
  j = getInputValido("Digite a coluna: ")

  """
  Opação teste automático:

  i = randint(0,3)
  j = randint(0,3)
  print("\n\n\n")
  """

  if(verificaMovimento(board, i, j)):
    fazMovimento(board, i ,j, jogador)
    jogador = (jogador + 1)%2
  else:
    print("A posicao informada ja esta ocupada")
  ganhador = verificaGanhador(board)

print("--------------------")
printBoard(board)
if ganhador != 'EMPATE': print(f"O '{ganhador}' venceu!!") 
else: print("**EMPATE**")
print("--------------------")