def main():
    nome = input("Qual é o seu nome? ")
    # Chamada da função
    ola(nome)

# voce pode usar def em python para definir suas próprias funções
# Nesse caso foi criada uma função chamada ola, que imprime na tela "Olá, ",
# com um espaço no final pois end=" ".
# Ola recebe um argumento chamado para receber o nome digitado pelo usuario.


def ola(pessoa):
    print("Olá,", pessoa)


main()
