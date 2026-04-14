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

# 🔹 Menu principal
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")