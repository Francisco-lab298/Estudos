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
def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")

    usuarios.append({
        "nome": nome,
        "idade": idade
    })

    salvar()
    print("✅ Usuário cadastrado!\n")

# 🔹 Listar usuários
def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    print("\n📋 Lista de usuários:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {u['nome']} | Idade: {u['idade']}")
    print()

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