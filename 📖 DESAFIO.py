# Escrita
with open("usuarios.txt", "w") as arquivo:
    for i in range(3):
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        arquivo.write(nome + "," + idade + "\n")

# Leitura (fora do loop!)
with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(",")
        print(f"Nome: {nome}, Idade: {idade}")
