op = input('Введите операцию: ')
a1 = int(input('Введите 1-ое число: '))
a2 = int(input('Введите 2-ое число: '))
def calculator(operation, a, b):
    if operation == '*':
        return a * b
    elif operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            print('Делить на ноль нельзя!')

print(calculator(op, a1, a2))
