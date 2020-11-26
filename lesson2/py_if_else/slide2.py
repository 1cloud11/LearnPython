
#test_list = [
#    {'str1': 'Python', 'str2': 'learn'}, 
#    {'str1': 'четыре', 'str2': 'два'}, 
#    {'str1': 2, 'str2': 4}, 
#    {'str1': 'три', 'str2': 'три'},     
#    {'str1': 'кот', 'str2': 'кошка'}
#    ]


def str_comp(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif len(str1) > len(str2) and str2 != 'learn':
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3    
    else: 
        return 0

#Автопроверка с использованием данных в списке словарей list:
#for i in range(len(test_list)):
#    print(str_comp(test_list[i]['str1'], test_list[i]['str2']))

first_str = (input('Пожалуйста, введите первую строку: '))
second_str = (input('Пожалуйста, введите вторую строку: '))

print(str_comp(first_str, second_str))