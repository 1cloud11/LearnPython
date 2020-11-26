talks = {
    'Привет!': 'Здарова',
    'Как дела?': 'По тихонечку',
    'Чем занят?': 'Программирую',
    'И как?': 'Вроде норм'
}

def ask_user(question):
    print(talks.get(question))

while True:
    ask_user(input())