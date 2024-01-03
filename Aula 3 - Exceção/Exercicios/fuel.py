def main():
    fração = input("Fração: ")
    numerador, denominador = fração.split("/")
    try:
        int_numerador = int(numerador)
        int_denominador = int(denominador)
        porcentagem = int_numerador/int_denominador*100
    except ValueError:
        main()
    except ZeroDivisionError:
        main()
    else:
        if porcentagem >= 99:
            print("F")
        elif porcentagem <= 1:
            print("E")
        else:
            print(f"Porcentagem: {porcentagem:.0f} %")


main()
