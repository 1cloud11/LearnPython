v = int(input('Введите число от 1 до 10: '))
if v > 10 or v < 0:
    print('От 1 до 10!!!')
else:
    print(v+10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print(' float(\'1\') результат 1.0')
print('int(\'2.5\') результат ошибка invalid literal for int() with base 10: \'2.5')
print('bool(1) результат True') 
print('bool('') результат False')
print('bool(0) результат False')