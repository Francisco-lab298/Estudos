while True:# O loop continua até que uma divisão seja realizada com sucesso'
    try:# O bloco de código dentro do try é onde a divisão é realizada. Se ocorrer um erro, ele será capturado pelos excepts.
        a = int(input("Numero 1: "))# O usuário é solicitado a digitar o primeiro número, que é convertido para um inteiro. Se o usuário digitar algo que não seja um número inteiro, um ValueError será levantado.
        b = int(input("Numero 2: "))
        print(a/b)# O resultado da divisão é impresso. Se o segundo número for zero, um ZeroDivisionError será levantado.
        break# Se a divisão for realizada com sucesso, o loop é interrompido com break.
    except ValueError:# Este bloco captura o erro específico de ValueError, que ocorre quando a conversão para inteiro falha.
        print("Por favor, digite apenas números inteiros.")# O usuário é informado sobre o erro e o loop continua, permitindo que ele tente novamente.
    except ZeroDivisionError:# Este bloco captura o erro específico de ZeroDivisionError, que ocorre quando o segundo número é zero.
        print("O segundo número não pode ser zero.")# O usuário é informado sobre o erro e o loop continua, permitindo que ele tente novamente.
    except Exception as e:# Este bloco captura qualquer outro tipo de exceção que possa ocorrer, garantindo que o programa não falhe inesperadamente.
         print(f"Ocorreu um erro: {e}")# O usuário é informado sobre o erro específico que ocorreu, e o loop continua, permitindo que ele tente novamente.