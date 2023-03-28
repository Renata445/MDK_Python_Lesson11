def fibonacci():
    fib_list = [0, 1]
    num = 1

    while num < 100:
        num = fib_list[-1] + fib_list[-2]
        if num < 100:
            fib_list.append(num)

    return fib_list
x = fibonacci()
print(x)
print()


def fib(num1 = 0, num2 = 1):
    if num2 >= 100:
        return []

    return [num2] + fib(num2, num1 + num2)

x = fib()
print(x)
