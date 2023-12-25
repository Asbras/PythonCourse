"""
        In the US, its customary to leave a tip for your server after
    dining in a restaurant, typically an amount equal to 15% or more of your
    meal’s cost.
"""


def main():
    dollars = dollar_para_float(input("Qual foi o valor da sua conta? "))
    porcentagem = porcentagem_para_float(input("Quantos porcento voces gotaria de deixar de gorjeta? "))
    gorjeta = dollars * porcentagem
    print(f"Total: $ {gorjeta:.2f}")


def dollar_para_float(d):
    d = d.strip('$')
    return float(d)


def porcentagem_para_float(p):
    p = p.strip('%')
    return float(p)/100


main()
