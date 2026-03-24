while True:
    try:
        a = int(input("Numero 1: "))
        b = int(input("Numero 2: "))
        print(a/b)
        break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    except ZeroDivisionError:
        print("O segundo número não pode ser zero.")
    except Exception as e:
         print(f"Ocorreu um erro: {e}")