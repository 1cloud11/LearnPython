school_data = [
    {'school_class': '1a', 'scores': [3, 4, 5, 2, 5]},
    {'school_class': '2a', 'scores': [5, 2, 3, 3, 4]},
    {'school_class': '3a', 'scores': [4, 4, 4, 4, 4]},
    {'school_class': '4a', 'scores': [2, 3, 4, 5, 5]},
    {'school_class': '5a', 'scores': [5, 4, 3, 2, 2]}
]

school_sum = 0

for i in school_data:
    res = sum(i['scores'])/len(i['scores'])    
    school_sum += res

school_res = float('{0:2f}'.format(school_sum/len(school_data)))
print(f'Средний бал по школе составляет {school_res}')

for i in school_data:
    res = sum(i['scores'])/len(i['scores'])
    sclass = i['school_class']
    print(f'Средний бал для класса {sclass} составляет {res}')