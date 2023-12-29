"""
In deep.py, implement a program that prompts the user for the answer to the
Great Question of Life, the Universe and Everything, outputting Yes if the user
inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""
m = "What is the Answer to the Great Question of Life, the Universe, and Everything? "


def main():
    resposta = input(m)
    esta_correto(resposta)


def esta_correto(x):
    if x == "forty-two" or x == "forty two" or x == "42":
        print("Yes")
    else:
        print("No")


main()
