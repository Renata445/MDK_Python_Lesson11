def count():
    even_num = 0
    odd_num = 0
    num = 0
    while num <= 10:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
        num += 1
    print(f'Кол-во четных чисел: {even_num}')
    print(f'Кол-во нечетных чисел: {odd_num}')

count()
print()

def count1(num = 0, even_num = 0, odd_num = 0):
    if num > 10:
        print(f'Кол-во четных чисел: {even_num}')
        print(f'Кол-во нечетных чисел: {odd_num}')
        return
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    count1(num + 1, even_num, odd_num)
count1()
