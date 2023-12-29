def main():
    mensagem = input("Input: ")
    mensagem_sem_vogais = retirar_vogais(mensagem)
    print("Output: ", mensagem_sem_vogais)


def retirar_vogais(m):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    mensagem_sem_vogal = ""
    for letra in m:
        if letra not in vogais:
            mensagem_sem_vogal += letra
    return mensagem_sem_vogal


main()
