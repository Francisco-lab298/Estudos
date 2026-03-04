pessoas = []# Crie um programa que permita ao usuário cadastrar informações de 3 pessoas, incluindo nome e idade. Em seguida, exiba as informações cadastradas.

for i in range(3):# Loop para cadastrar informações de 3 pessoas
    usuario = {}# Dicionário para armazenar as informações de cada pessoa
    usuario["nome"] = input("Digite seu nome: ")# Solicita ao usuário que digite seu nome e armazena no dicionário
    usuario["idade"] = int(input("Digite sua idade: "))# Solicita ao usuário que digite sua idade, converte para inteiro e armazena no dicionário
    pessoas.append(usuario)# Adiciona o dicionário com as informações da pessoa à lista de pessoas

print("\nPessoas cadastradas:")# Exibe um título para a seção de pessoas cadastradas
for pessoa in pessoas:# Loop para exibir as informações de cada pessoa cadastrada
    print(pessoa["nome"], pessoa["idade"])# Exibe o nome e a idade de cada pessoa cadastrada
