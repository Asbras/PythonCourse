"""
In a file called extensions.py, implement a program that prompts the user for
he name of a file and then outputs that file’s media type if the file’s name
ends, case-insensitively, in any of these suffixes:
    1 .gif
    2 .jpg
    3 .jpeg
    4 .png
    5 .pdf
    6 .txt
    7 .zip
"""


def main():
    arquivo = input("Nome do arquivo: ")
    categorizar(arquivo)


def categorizar(a):
    nome, separador, extencao = a.partition('.')
    match extencao:
        case "gif":
            print("Imagem/gif")
        case "jpeg":
            print("Imagem/jpeg")
        case "jpg":
            print("Imagem/jpeg")
        case "txt":
            print("Texto/txt")
        case "png":
            print("Imagem/png")
        case "pdf":
            print("Documento/pdf")
        case "zip":
            print("Arquivo/zip")
        case _:
            print("Applicação/octet-stream")


main()
