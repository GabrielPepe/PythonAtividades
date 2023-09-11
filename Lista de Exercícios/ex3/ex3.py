import random
from termcolor import colored
from unidecode import unidecode

"""
Função que define qual palavra será utilizada
"""
def escolher_palavra():
    with open("ex3/lista_palavras.txt", "r") as arquivo:
        palavras = [unidecode(linha.strip()) for linha in arquivo if len(linha.strip()) == 5]
    return random.choice(palavras)

"""
Mostra no terminal a palavra da tentativa
as letras que aparecerem em amarelo estão
contidas na palavra final porem na posicão
errada, já as em verde estão na correta
"""
def mostrar_palavra(palavra, tentativa):
    resultado = ""
    for i in range(len(palavra)):
        if palavra[i] == tentativa[i]:
            resultado += colored(palavra[i], 'green') 
        elif tentativa[i] in palavra:
            resultado += colored(tentativa[i], 'yellow')
        else:
            resultado += tentativa[i]
    return resultado

"""
Onde irá ser executado o código e 
as outras funções
"""
def main():
    max_tentativas = 6
    palavra_a_adivinhar = escolher_palavra()
    
    print("Bem-vindo ao Wordle!")
    print(f"Você tem {max_tentativas} tentativas para adivinhar a palavra secreta de 5 letras.")
    
    while max_tentativas > 0:
        tentativa = input("\nDigite sua tentativa de palavra: ").lower()
        

        """
        Define se a tentativa é igual a palavra final
        em caso afirmativo, o jogador vence
        """
        if len(tentativa) == 5 and tentativa.isalpha():
            tentativa_sem_acentos = unidecode(tentativa)
            if tentativa_sem_acentos == palavra_a_adivinhar:
                print("Parabéns! Você acertou a palavra secreta!")
                break
            else:
                max_tentativas -= 1
                print(f"Tentativas restantes: {max_tentativas}")
                resultado = mostrar_palavra(palavra_a_adivinhar, tentativa_sem_acentos)
                print(f"Palavra atual: {resultado}")
        else:
            print("Entrada inválida. Digite uma palavra de 5 letras.")

    if max_tentativas == 0:
        print(f"Fim de jogo! A palavra secreta era '{palavra_a_adivinhar}'.")

if __name__ == "__main__":
    main()