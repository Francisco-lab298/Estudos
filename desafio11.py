import json

ARQUIVO = "usuarios.json"

# 🔹 Carregar dados (se existir)
try:#
    with open(ARQUIVO, "r") as f:
        usuarios = json.load(f)
except:#
    usuarios = []#

# 🔹 Função para salvar
def salvar():#
    with open(ARQUIVO, "w") as f:#
        json.dump(usuarios, f, indent=4)#

# 🔹 Cadastrar usuário
def cadastrar():#
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

# 🔹 Editar usuário
def editar():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['idade']}")

    try:
        indice = int(input("Digite o número do usuário que deseja editar: "))

        if 1 <= indice <= len(usuarios):
            usuario = usuarios[indice - 1]

            print(f"\nEditando: {usuario['nome']}")

            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")

            usuario["nome"] = novo_nome
            usuario["idade"] = nova_idade

            salvar()

            print("✅ Usuário atualizado com sucesso!\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Digite apenas números.\n")

# 🔹 Deletar usuário
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
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")