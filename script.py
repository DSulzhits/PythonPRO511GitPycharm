def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def exponent(a, b):
    if type(b) is int:
        return a ** b
    return f'Степень может быть только целым числом!'


if __name__ == '__main__':
    print(add(3, 5))
    print(multiply(3, 5))
    print(exponent(4, 3))
