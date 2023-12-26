"""
    Python already supports math, whereby you can write code to add, subtract,
    multiply, or divide values and even variables. But let’s write a program 
    that enables users to do math, even without knowing Python.

    In a file called interpreter.py, implement a program that prompts the user 
    for an arithmetic expression and then calculates and outputs the result as
    a floating-point value formatted to one decimal place.
    Assume that the user’s input will be formatted as x y z, with one space 
    between x and y and one space between y and z, wherein:
        x is integer
        y is +,-,*,/
        z is integer
"""


def main():
    expression = input("Expressão: ")
    x, y, z = expression.split(" ")
    match y:
        case "+":
            resultado = float(int(x) + int(z))
            print("{:.1f}".format(resultado))
        case "-":
            resultado = float(int(x) - int(z))
            print("{:.1f}".format(resultado))
        case "*":
            resultado = float(int(x) * int(z))
            print("{:.1f}".format(resultado))
        case "/":
            resultado = float(int(x) / int(z))
            print("{:.1f}".format(resultado))
        case _:
            print("Não entendi")


main()
