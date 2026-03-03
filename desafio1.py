cadastro = []# Lista para armazenar os nomes cadastrados

for i in range(5):# Loop para solicitar o cadastro de 5 nomes
    nome = input("Digite seu nome: ")# Solicita ao usuário que digite seu nome
    cadastro.append(nome)# Adiciona o nome digitado à lista de cadastro
    
print("Nomes cadastrados:")# Imprime uma mensagem indicando que os nomes cadastrados serão exibidos
for nome in cadastro:# Loop para percorrer a lista de cadastro e imprimir cada nome
    print(nome)# Imprime o nome atual da lista de cadastro