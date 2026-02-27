# Escrita #com o "with", o arquivo é fechado automaticamente após o bloco de código
with open("usuarios.txt", "w") as arquivo:
    for i in range(3):
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        arquivo.write(nome + "," + idade + "\n")

# Leitura (fora do loop!)
with open("usuarios.txt", "r") as arquivo:# O código acima abre o arquivo "usuarios.txt" para leitura usando o modo "r". Em seguida, ele itera sobre cada linha do arquivo usando um loop for. Para cada linha, ele remove os espaços em branco no início e no final da linha usando o método strip() e divide a linha em duas partes usando a vírgula como separador com o método split(","). O nome é atribuído à variável "nome" e a idade à variável "idade". Por fim, o código imprime o nome e a idade de cada usuário.
    for linha in arquivo:# O código acima abre o arquivo "usuarios.txt" para leitura e itera sobre cada linha do arquivo. Para cada linha, ele remove os espaços em branco no início e no final da linha usando o método strip() e, em seguida, divide a linha em duas partes usando a vírgula como separador com o método split(","). O nome é atribuído à variável "nome" e a idade à variável "idade". Por fim, o código imprime o nome e a idade de cada usuário.
        nome, idade = linha.strip().split(",")# O método strip() remove os espaços em branco no início e no final da linha, e o método split(",") divide a linha em duas partes usando a vírgula como separador, atribuindo o nome à variável "nome" e a idade à variável "idade".
        print(f"Nome: {nome}, Idade: {idade}")# O código acima cria um arquivo chamado "usuarios.txt" e escreve o nome e a idade de três usuários, separados por vírgula. Em seguida, ele lê o arquivo e imprime o nome e a idade de cada usuário.
