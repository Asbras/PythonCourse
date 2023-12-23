# Perguntar o nome do usuário
nome = input("Qual o seu nome? ")

# Remover espaçoes em branco da string nome
nome = nome.strip()

# Deixar a primeira letra do nome maiúscula da primeira palavra
nome = nome.capitalize()

# Você pode usar também o .title que irá deixar TODAS  as letras iniciais de palavras em maiúculo.
nome = nome.title()

# Podemos usar também varias funções de uma vez só
nome = nome.strip().title()

# Imprimir Olá para o usuário com o nome
print(f"Olá, {nome}")
