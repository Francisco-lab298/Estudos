import json

ARQUIVO = "usuarios.json"

# 🔹 Carregar dados (se existir)
try:
    with open(ARQUIVO, "r") as f:
        usuarios = json.load(f)
except:
    usuarios = []

# 🔹 Função para salvar
def salvar():
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

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