# Um dicionário em Python é uma coleção de pares chave-valor, onde cada chave
# única leva a um valor. É mutável, flexível e usado para armazenar e organizar
# dados de forma eficiente.
estudantes = {
    "Hermione": "Griffinória",
    "Harry": "Griffinória",
    "Ron": "Griffinória",
    "Draco": "Sonserina",
}


for estudante in estudantes:
    print(estudante, estudantes[estudante], sep=", ")
# se a variavel nao for importante pordemos usar _ para sinalizar que só é necessario para contar.
for _ in range(3):
    print("meow")
# voce tambem pode imprimir varias vezes simplesmente "multiplicando" a quantidade de vezes quantidade
# que voce deseja imprimir
print("meow\n" * 3, end="")
#
def main():
    numero = receber_numero()
    meow(numero)


def receber_numero():
    while True:
        n = int(input("Quantas vezes o gato miou? "))
        if n > 0:
            return n
            break


def meow(i):
    print("meow\n" * i, end="")


main()
# Listas sempre usam []
estudantes = ["Hermione", "Harry", "Ron"]

for estudante in estudantes:
    print(estudante)

# ou se voce necessitar de uma variavel para contar
# voce também pode usar

estudantes = ["Hermione", "Harry", "Ron"]
# A função len retorna o tamanho da string
for i in range(len(estudantes)):
    print(i + 1, estudantes[i])
#
estudantes = [
    {"nome": "Hermione", "casa": "Grifinória", "patrono": "Lontra"},
    {"nome": "Harry", "casa": "Grifinória", "patrono": "Cervo"},
    {"nome": "Rony", "casa": "Grifinória", "patrono": "Cachorro"},
    {"nome": "Draco", "casa": "Sonserina", "patrono": None}
]

for estudante in estudantes:
    print(estudante["nome"], estudante["casa"], estudante["patrono"], sep=", ")
def main():
    imprimir_quadrado(3)


def imprimir_coluna(altura):
    print("#\n" * altura, end="")


def imprimir_linha(largura):
    print("#" * largura)


def imprimir_quadrado(tamanho):
    for i in range(tamanho):
        imprimir_linha(tamanho)


main()
# Validar se o usuário esta digitando um valor positivo
while True:
    n = int(input("Qual o valor de n? "))
    if n > 0:
        break

print("Meow\n" * n, end="")
# (i += 1) == (i = i + 1)
i = 0
while i < 3:
    print("Meow")
    i += 1
