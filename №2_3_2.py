seasons = {
    'Зима': (1, 2, 12),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}
try:
    user_query = int(input('Введите номер месяца: '))
except ValueError:
    print('Некорректный ввод')
else:
    if user_query in range(1, 13):
        for key in seasons.keys():
            if user_query in seasons[key]:
                print(key)
    else:
        print('В году только 12 месяцев')
