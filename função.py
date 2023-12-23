# voce pode usar def em python para definir suas próprias funções
# Nesse caso foi criada uma função chamada ola, que imprime na tela "Olá, ", com um espaço no final pois end=" ".
def ola():
    print("Olá,", end=" ")
name = input("Qual é o seu nome? ")
# Chamada da função
ola()
print(name)
