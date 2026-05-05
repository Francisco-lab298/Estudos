import json

ARQUIVO = "usuarios.json"# Desafio 11: Cadastro de Usuários com Persistência

# 🔹 Carregar dados (se existir)
try:# Tenta abrir o arquivo e carregar os usuários. Se o arquivo não existir, inicia com uma lista vazia.
    with open(ARQUIVO, "r") as f:# Abre o arquivo em modo leitura.
        usuarios = json.load(f)# Carrega os dados do arquivo JSON para a variável 'usuarios'.
except:# Se ocorrer um erro (como o arquivo não existir), inicializa 'usuarios' como uma lista vazia.
    usuarios = []#print("Bem-vindo ao sistema de cadastro de usuários!\n")

# 🔹 Função para salvar
def salvar():# Abre o arquivo em modo escrita e salva a lista de usuários no formato JSON, com indentação para melhor leitura.
    with open(ARQUIVO, "w") as f:# Abre o arquivo em modo escrita.
        json.dump(usuarios, f, indent=4)# Salva a lista de usuários no arquivo JSON, formatando com indentação para facilitar a leitura.

# 🔹 Cadastrar usuário
def cadastrar():# Solicita ao usuário que insira o nome e a idade, e depois adiciona um novo dicionário com essas informações à lista de usuários. Em seguida, chama a função 'salvar()' para persistir os dados no arquivo.
    nome = input("Nome: ")# Solicita ao usuário que insira o nome e armazena na variável 'nome'.
    idade = input("Idade: ")# Solicita ao usuário que insira a idade e armazena na variável 'idade'.

    usuarios.append({# Adiciona um novo dicionário com as chaves "nome" e "idade" à lista de usuários.
        "nome": nome,# A chave "nome" recebe o valor da variável 'nome'.
        "idade": idade# A chave "idade" recebe o valor da variável 'idade'.
    })

    salvar()# Chama a função 'salvar()' para salvar a lista de usuários atualizada no arquivo JSON.
    print("✅ Usuário cadastrado!\n")# Exibe uma mensagem de confirmação de que o usuário foi cadastrado com sucesso.

# 🔹 Listar usuários
def listar():#  Verifica se a lista de usuários está vazia. Se estiver, exibe uma mensagem informando que nenhum usuário está cadastrado. Caso contrário, itera sobre a lista de usuários e exibe o nome e a idade de cada um.
    if not usuarios:# Verifica se a lista de usuários está vazia. Se estiver, exibe uma mensagem informando que nenhum usuário está cadastrado e retorna da função.
        print("Nenhum usuário cadastrado.\n")# Exibe uma mensagem informando que nenhum usuário está cadastrado.
        return# Retorna da função, encerrando a execução do restante do código.

    print("\n📋 Lista de usuários:")# Exibe o cabeçalho da lista de usuários.
    for i, u in enumerate(usuarios, start=1):# Itera sobre a lista de usuários usando a função 'enumerate()' para obter o índice (começando em 1) e o usuário (um dicionário). Para cada usuário, exibe o índice, o nome e a idade formatados.
        print(f"{i}. Nome: {u['nome']} | Idade: {u['idade']}")# Exibe o índice, o nome e a idade do usuário formatados.
    print()# Exibe uma linha em branco para melhor formatação.
def deletar():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['idade']}")

    try:
        indice = int(input("Digite o número do usuário que deseja deletar: "))

        if 1 <= indice <= len(usuarios):
            removido = usuarios.pop(indice - 1)
            salvar()
            print(f"{removido['nome']} foi removido.\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Digite apenas números.\n")

# 🔹 Menu principal
while True:# Inicia um loop infinito para exibir o menu principal e processar as opções do usuário.
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Deletar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")# Solicita ao usuário que escolha uma opção e armazena a entrada na variável 'opcao'.

    if opcao == "1":# Se a opção escolhida for "1", chama a função 'cadastrar()' para cadastrar um novo usuário.
        cadastrar()# Se a opção escolhida for "2", chama a função 'listar()' para exibir a lista de usuários cadastrados.
    elif opcao == "2":# Se a opção escolhida for "3", exibe uma mensagem de saída e quebra o loop para encerrar o programa.
        listar()#
    elif opcao == "3":
        deletar()
    elif opcao == "4":#
        print("Saindo...")# Exibe uma mensagem de saída.
        break# Quebra o loop para encerrar o programa.
    else:
        print("Opção inválida!\n")# Exibe uma mensagem de opção inválida e uma linha em branco para melhor formatação.
        
def deletar():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['idade']}")

    try:
        indice = int(input("Digite o número do usuário que deseja deletar: "))

        if 1 <= indice <= len(usuarios):
            removido = usuarios.pop(indice - 1)
            salvar()
            print(f"{removido['nome']} foi removido.\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Digite apenas números.\n")