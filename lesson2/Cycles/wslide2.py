talks = {
    'Привет!': 'Здарова',
    'Как дела?': 'По тихонечку',
    'Чем занят?': 'Программирую',
    'И как?': 'Вроде норм'
}

def ask_user(question):
    for i in talks:
        if i == question:
            print(talks[i])

while True:
    ask_user(input())