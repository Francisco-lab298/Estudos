cadastro = []

for i in range(5):
    nome = input("Digite seu nome: ")
    cadastro.append(nome)
    
print("Nomes cadastrados:")
for nome in cadastro:
    print(nome)