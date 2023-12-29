"""
"""


def main():
    nota = int(input("Digite sua nota de 0 a 100: "))

    if nota >= 90:
        print("Nota: A")
    elif nota >= 80:
        print("Nota: B")
    elif nota <= 70:
        print("Nota: C")
    elif nota <= 60:
        print("Nota: D")
    else:
        print("Nota: F")


main()
"""
O uso  elif (else if) é útil para criar uma cadeia de verificações
exclusivas, onde apenas um bloco de código é executado entre várias condições
mutuamente exclusivas. Isso torna o código mais organizado e eficiente,
evitando verificações desnecessárias após uma condição já ter sido atendida.
"""


def main():
    x = int(input("Qual o valor de X?"))
    y = int(input("Qual o valor de Y?"))

    if x < y:
        print("x é menor que y")
    elif x > y:
        print("x é maior que y")
    elif x == y:
        print("x é igual que y")


main()
"""
    Neste caso voce pode usar o else no final, pois
    não há outra opção, portanto não há necessidade
    de testar se x é igual a y.
"""


def main():
    x = int(input("Qual o valor de X?"))
    y = int(input("Qual o valor de Y?"))

    if x < y:
        print("x é menor que y")
    elif x > y:
        print("x é maior que y")
    else:
        print("x é igual que y")


main()
"""

"""

name = input("Qual o nome do personagem")

match name:
    case "Harry" | "Hermione" | "Rony":
        print("Griffinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Quem?")


def main():
    x = int(input("Qual o valor de X?"))
    y = int(input("Qual o valor de Y?"))

    if x < y:
        print("x é menor que y")

    if x > y:
        print("x é maior que y")

    if x == y:
        print("x é igual que y")


main()
"""
"""


def main():
    x = int(input("Digite um número qualquer: "))
    if eh_par(x):
        print("Par")
    else:
        print("Impar")


def eh_par(n):
    return n % 2 == 0


main()
"""
"""


def main():
    x = int(input("Qual o valor de X?"))
    y = int(input("Qual o valor de Y?"))

    if x < y or x > y:
        print("X não é igual a y")
    else:
        print("x é igual a y")


main()
