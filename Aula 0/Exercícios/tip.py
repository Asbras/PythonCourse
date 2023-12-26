"""
        In the US, its customary to leave a tip for your server after
    dining in a restaurant, typically an amount equal to 15% or more of your
    meal’s cost.
"""


def main(dollar_input, porcentagem_input):
    dollars = dollar_para_float(dollar_input)
    porcentagem = porcentagem_para_float(porcentagem_input)
    gorjeta = dollars * porcentagem
    return f"Total: $ {gorjeta:.2f}"


def dollar_para_float(d):
    d = d.strip('$')
    return float(d)


def porcentagem_para_float(p):
    p = p.strip('%')
    return float(p)/100


main()
