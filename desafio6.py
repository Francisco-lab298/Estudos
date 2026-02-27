pessoas = []# O código acima cria uma lista vazia chamada "pessoas". Em seguida, ele solicita ao usuário que insira o nome e a idade de três pessoas, armazenando essas informações em dicionários. Cada dicionário é adicionado à lista "pessoas". Por fim, o código imprime o nome e a idade de cada pessoa na lista, bem como a lista completa de pessoas.

usuario = {}# O código acima cria um dicionário vazio chamado "usuario". Em seguida, ele solicita ao usuário que insira seu nome e idade, armazenando essas informações no dicionário. O dicionário é então adicionado à lista "pessoas".
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
    
print(pessoas)# O código acima cria uma lista chamada "pessoas" e adiciona três dicionários, cada um representando um usuário com seu nome e idade. Em seguida, o código imprime o nome e a idade de cada pessoa na lista, bem como a lista completa de pessoas.