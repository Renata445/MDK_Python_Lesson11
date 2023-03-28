n = int(input('ведите число: '))

def factorial(num):
    i = 1
    while num > 1:
        i *= num
        num -= 1

    print(i)

factorial(n)
print()
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(fac(n))
