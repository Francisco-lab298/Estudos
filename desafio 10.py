import json

cadastro = {}
for i in range(3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cadastro[nome] = idade

with open("cadastro.json", "w") as f:
    json.dump(cadastro, f)

with open("cadastro.json", "r") as f:
    cadastro = json.load(f)

print(cadastro)