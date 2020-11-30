from datetime import datetime, date, timedelta

today = date.today()
delta = timedelta(days=1)
yesterday = today - delta
month_ago = today - delta*30

print(f'Вчера было {yesterday}')
print(f'Сегодня {today}')
print(f'30 дней назад было {month_ago}')

string = "01/01/25 12:10:03.234567"
string_date = datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
print(type(string_date))