def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    return f'На ноль делить нельзя!'


def exponent(a, b):
    if type(b) is int:
        return a ** b
    return f'Степень может быть только целым числом!'


if __name__ == '__main__':
    print(add(3, 5))
    print(multiply(3, 5))
    print(divide(10, 2))
    print(exponent(5, 3))
