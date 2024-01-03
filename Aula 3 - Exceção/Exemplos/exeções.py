while True:
    try:
        x = int(input("Qual o valor de x? "))
    except ValueError:
        print("x não é um inteiro")
    else:
        break

print(f"x é {x}")
