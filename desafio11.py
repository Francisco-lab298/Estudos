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
        print("Nenhum usuário cadastrado.\n")# Verifica se a lista de usuários está vazia. Se estiver, exibe uma mensagem informando que nenhum usuário está cadastrado e retorna da função.
        return# Retorna da função, encerrando a execução do restante do código.

    print("\nUsuários cadastrados:")# Exibe o cabeçalho da lista de usuários cadastrados.
    for i, u in enumerate(usuarios, start=1):# Itera sobre a lista de usuários usando a função 'enumerate()' para obter o índice (começando em 1) e o usuário (um dicionário). Para cada usuário, exibe o índice, o nome e a idade formatados.
        print(f"{i}. {u['nome']} - {u['idade']}")# Exibe o índice, o nome e a idade do usuário formatados.

    try:# Tenta converter a entrada do usuário para um número inteiro. Se a conversão falhar (por exemplo, se o usuário digitar algo que não seja um número), captura a exceção ValueError e exibe uma mensagem de erro.
        indice = int(input("Digite o número do usuário que deseja deletar: "))# Solicita ao usuário que digite o número do usuário que deseja deletar e tenta converter essa entrada para um número inteiro, armazenando o resultado na variável 'indice'.

        if 1 <= indice <= len(usuarios):# Verifica se o número digitado pelo usuário está dentro do intervalo válido (entre 1 e o número total de usuários). Se estiver, remove o usuário correspondente da lista usando o método 'pop()' e armazena o usuário removido na variável 'removido'. Em seguida, chama a função 'salvar()' para atualizar o arquivo JSON e exibe uma mensagem confirmando que o usuário foi removido.
            removido = usuarios.pop(indice - 1)# Remove o usuário correspondente ao índice fornecido (ajustado para zero-based) da lista de usuários e armazena o usuário removido na variável 'removido'.
            salvar()# Chama a função 'salvar()' para salvar a lista de usuários atualizada no arquivo JSON.
            print(f"{removido['nome']} foi removido.\n")# Exibe uma mensagem confirmando que o usuário foi removido, mostrando o nome do usuário removido.
        else:# Se o número digitado pelo usuário não estiver dentro do intervalo válido, exibe uma mensagem de número inválido.
            print("Número inválido.\n")# Exibe uma mensagem de número inválido e uma linha em branco para melhor formatação.

    except ValueError:# Captura a exceção ValueError que ocorre quando a conversão para inteiro falha (por exemplo, se o usuário digitar algo que não seja um número) e exibe uma mensagem de erro.
        print("Digite apenas números.\n")# Exibe uma mensagem de erro informando que o usuário deve digitar apenas números, seguida de uma linha em branco para melhor formatação.

# 🔹 Menu principal
while True:# Inicia um loop infinito para exibir o menu principal e processar as opções do usuário.
    print("1 - Cadastrar")# Exibe as opções do menu para o usuário escolher.
    print("2 - Listar")# Exibe as opções do menu para o usuário escolher.
    print("3 - Deletar")# Exibe as opções do menu para o usuário escolher.
    print("4 - Sair")# Exibe as opções do menu para o usuário escolher.

    opcao = input("Escolha uma opção: ")# Solicita ao usuário que escolha uma opção e armazena a entrada na variável 'opcao'.

    if opcao == "1":# Se a opção escolhida for "1", chama a função 'cadastrar()' para cadastrar um novo usuário.
        cadastrar()# Se a opção escolhida for "2", chama a função 'listar()' para exibir a lista de usuários cadastrados.
    elif opcao == "2":# Se a opção escolhida for "3", exibe uma mensagem de saída e quebra o loop para encerrar o programa.
        listar()#
    elif opcao == "3":#
        deletar()#
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