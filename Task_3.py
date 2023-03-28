def hello(name):
    lst_name = []
    if name in lst_name:
        print(f'Привет, {name}!')
    else:
        print(f'Привет, {name}! Рад знакомству!')
        lst_name.append(name)
hello(n)
