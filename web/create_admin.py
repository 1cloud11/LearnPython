from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input("Введите имя: ")

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем уже есть')
        sys.exit(0)

    password = getpass('Введите пароль')
    password2 = getpass('Повторите пароль')

    if not password == password2:
        print('Пароли не совпадают.')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'Создан пользователь с id: {new_user.id}')

#ошибка при внесении данных в дб, нужно исправить