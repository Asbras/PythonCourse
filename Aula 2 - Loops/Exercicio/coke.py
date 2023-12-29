def main():
    valor_total_inserido = 0
    while valor_total_inserido < 50:
        moeda_inserida = inserir_moeda()
        valor_total_inserido += moeda_inserida
        if 50 - valor_total_inserido > 0:
            print(f"Faltando: {50 - valor_total_inserido} centavos")
    print(f"Troco: {valor_total_inserido - 50}")


def inserir_moeda():
    while True:
        n = int(input("Insira uma moeda? "))
        if n == 25 or n == 10 or n == 5:
            return n


main()
