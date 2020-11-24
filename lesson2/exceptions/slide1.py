def hello_user():
    try:
        while True:
            user_say = input('Как дела? ')
            if user_say == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('Пока!')

hello_user()