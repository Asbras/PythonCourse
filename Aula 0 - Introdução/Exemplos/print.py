# De acordo com a documentação do python a função print funciona dessa maneira e voce pode mudar o valor de 
# todos esses parametros
# print(*objects, sep=' ', end='\n', fyle=sys.stdout, flush=False)

# Recebe o nome que o usuário digitar e guarda na variavel nome.
nome = input("Qual é o seu nome?\n")

# Escrever na tela o Olá, nome escrito pelo usuário voce tambem pode usar print("Olá," + nome) 
print("Olá,", nome)

# Outra maneira de fazer o mesmo é usando o paramero end
print("Olá, ", end="")
print(nome)

# Mais uma maneira de escrever o mesmo
print(f"Olá, {nome}") 
