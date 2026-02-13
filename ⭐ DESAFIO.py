pessoas = []

for i in range(3):
    usuario = {}
    usuario["nome"] = input("Digite seu nome: ")
    usuario["idade"] = int(input("Digite sua idade: "))
    pessoas.append(usuario)

print("\nPessoas cadastradas:")
for pessoa in pessoas:
    print(pessoa["nome"], pessoa["idade"])
