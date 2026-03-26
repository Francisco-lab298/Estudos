def maior(a, b):# Esta função recebe dois números como parâmetros e retorna o maior entre eles.
    """Retorna o maior entre dois números."""# A docstring explica o propósito da função, indicando que ela retorna o maior entre dois números.
    if a > b:# A condição verifica se o primeiro número (a) é maior que o segundo número (b).
        return a# Se a condição for verdadeira, a função retorna o valor de a, que é o maior número.
    else:# Se a condição for falsa, ou seja, se b for maior ou igual a a, o código dentro do bloco else será executado.
        return b# Se a condição for falsa, a função retorna o valor de b, que é o maior número ou igual a a.
    
print(maior(10, 20))  # Exemplo de uso da função