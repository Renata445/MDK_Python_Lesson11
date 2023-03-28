def login():
    users = {'Grek': '1234', 'Lalita': '1256', 'RenMar': '5612'}
    username = input('Введите логин: ')
    password = input('Введите пароль: ')
    if username in users:
        if users[username] == password:
            print('Доступ разрешен')
        else:
            print('Доступ запрещен')
    else:
        users[username] = password
        print('Регистрация прошла успешно!')

login()
