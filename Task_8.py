from random import randint
x = randint(0, 100)
print(x)
def Guess_the_number(x, guess, i):
    guess = int(input('Введите число, которое вы думаете: '))
    if guess == x:
        print(f'Поздравляю, ты угадал загаданное число {guess} с {i} попытки!')
        return
    elif i == 10:
        print('Вы исчерпали свои попытки!')
    elif guess > x:
        print('Вы ввели большее число, чем загадал компьютер!')
        Guess_the_number(x, guess, i + 1)
    elif guess < x:
        print('Вы ввели меньшее число, чем загадал компьютер!')
        Guess_the_number(x, guess, i + 1)

Guess_the_number(x, 0, 1)
