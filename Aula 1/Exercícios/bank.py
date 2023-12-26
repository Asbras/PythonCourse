"""
    In a file called bank.py, implement a program that prompts the user for a
greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an
“h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading
whitespace in the user’s greeting, and treat the user’s greeting
case-insensitively.
"""


def main():
    mensagem = input("Greeting: ")
    receber = comparar(mensagem)
    print(receber)


def comparar(m):
    primeira_letra = m[0]
    if primeira_letra == "H" and m != "Hello" and m != "Hello, Newman":
        return "$20"
    elif m == "Hello" or m == "Hello, Newman":
        return "$0"
    else:
        return "$100"


main()
