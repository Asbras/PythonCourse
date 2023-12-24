"""
    In a file called faces.py, implement a function called convert that accepts a
 str as input and returns that same input with any :) converted to 🙂  and any
 :( converted to 🙁 . All other text should be returned unchanged.
"""
def faces(texto):
    texto_modificado = texto.replace(":)", "🙂")
    texto_modificado = texto_modificado.replace(":(", "🙁")
    return texto_modificado

def main():
    mensagem = input()
    mensagem = faces(mensagem)
    print(mensagem)


main()
