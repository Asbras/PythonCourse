"""
    Some people have a habit of speaking rather quickly, and it’d be nice to
    slow them down, a la YouTube’s 0.75 playback speed, or even by having them
    pause between words.
        In a file called playback.py, implement a program in Python that prompt
    the user for input and then outputs that same input, replacing each space
    with ... (i.e., three periods).
"""


def modificar(texto):
    texto_modificado = texto.replace(' ', '...')
    return texto_modificado


def main():
    mensagem = input()
    mensagem = modificar(mensagem)
    print(mensagem)


main()
