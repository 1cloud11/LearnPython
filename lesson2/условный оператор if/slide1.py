user_age = int(input('Пожалуйста, укаэите свой возраст: '))

def employement(age):
    if age <= 6:
        return 'Человек в детском саду'
    elif 6 < age <= 17:
        return 'Человек учится в школе'
    elif 17 < age <= 24:
        return 'Человек учится в ВУЗе'
    elif 24 < age <= 60:
        return 'Человек работает на работе'
    else:
        return 'Человек на заслуженном отдыхе'

res = employement(user_age)

print(res)
