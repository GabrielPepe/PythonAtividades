banco_usuarios = {}

"""
Função para cadastrar usuário
"""
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    for campo_obrigatorio in campos_obrigatorios:
        valor = input(f"Digite o valor para {campo_obrigatorio}: ")
        usuario[campo_obrigatorio] = valor
    while True:
        campo_adicional = input("Digite um campo adicional ou 'sair' para finalizar: ")
        if campo_adicional.lower() == 'sair':
            break
        """
        Caso seja diferente de 'sair', campo adicional 
        é criado automaticamente
        """
        valor_adicional = input(f"Digite o valor para {campo_adicional}: ")
        usuario[campo_adicional] = valor_adicional
    nome_usuario = usuario.get('nome')  # Isso supondo que 'nome' seria um campo obrigatório
    if nome_usuario:
        banco_usuarios[nome_usuario] = usuario
        print("Usuário cadastrado com sucesso!")
    else:
        print("Erro: Nome do usuário não encontrado.")

"""
Função para impressão dos usuários
"""
def imprimir_usuarios(*args, **kwargs):
    while True:
        print("\nOpções de impressão:")
        print("1 - Imprimir todos os usuários com todas as informações")
        print("2 - Imprimir dados de usuários pelos nomes especificados")
        print("3 - Filtrar e imprimir por campos e valores")
        print("4 - Voltar ao menu principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            """
            Imprime todos os campos
            """
            for nome, usuario in banco_usuarios.items():
                print(f"Nome: {nome}")
                print(usuario)
        elif escolha == "2":
            """
            Imprimir dados de usuários pelos nomes especificados
            """
            nomes = input("Digite os nomes dos usuários separados por vírgula: ").split(',')
            for nome in nomes:
                nome = nome.strip()
                if nome in banco_usuarios:
                    print(f"Nome: {nome}")
                    print(banco_usuarios[nome])
                else:
                    print(f"Usuário '{nome}' não encontrado.")
        elif escolha == "3":
            """
            iltrar e imprimir por campos e valores
            """
            campos_valores = {}
            while True:
                campo = input("Digite um campo (ou 'sair' para finalizar): ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Digite o valor para o campo '{campo}': ")
                campos_valores[campo] = valor

            """
            Testa se os dados são válidos para a impressão
            """
            for nome, usuario in banco_usuarios.items():
                atende_condicoes = True
                for campo, valor in campos_valores.items():
                    if campo not in usuario or usuario[campo] != valor:
                        atende_condicoes = False
                        break
                if atende_condicoes:
                    print(f"Nome: {nome}")
                    print(usuario)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

"""
Função principal
faz requisição das outras funções
"""
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por espaço: ").split()
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == "2":
            imprimir_usuarios()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()