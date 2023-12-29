def main():
    camel_case = input("camelCase: ")
    snake_case = converter(camel_case)
    print("snake_case:", snake_case)


def converter(s):
    snake_case = ""
    for char in s:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case


main()
