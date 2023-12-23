# Float é uma abreviação de ponto flutuante
# Esse é o mesmo programa que o inteiro.py, porem agora voce pode somar quaisquer numeros reais.
x = float(input("Qual é o valor de X? "))
y = float(input("Qual é o valor de Y? "))

z = round(x + y)
# Escrever na tela o resultado da x + y e formatar para colocar uma virgula a cada 3 algrarismos 
print(f"{z:,}")
