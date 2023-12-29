# Definir a função main,
# ela é responsável por pedir um valor para o usuário e
# retornar o quadrado do valor digitado.
def main():
    x = int(input("Qual o valor de X? "))
    # Chamar a função quadrado() e depois escrever na tela o valor retornado
    # pela função."
    print("O quadrado de x é", quadrado(x))


# Definir a função quadrado, que calcula o quadrado de um número
def quadrado(numero):
    return numero * numero


# Chamada da função main() para que o programa rode
main()
