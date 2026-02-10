pessoas = []

usuario = {}
usuario["nome"] = input("Digite seu nome: ")
usuario["idade"] = int(input("Digite sua idade: "))

usuario1 = {}
usuario1["nome"] = input("Digite seu nome: ")
usuario1["idade"] = int(input("Digite sua idade: "))

usuario2 = {}
usuario2["nome"] = input("Digite seu nome: ")
usuario2["idade"] = int(input("Digite sua idade: "))

pessoas.append(usuario)
pessoas.append(usuario1)
pessoas.append(usuario2)

for pessoa in pessoas:
    print(pessoa["nome"], pessoa["idade"])
    
print(pessoas)