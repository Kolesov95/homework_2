winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [10, 11, 12]
try:
    user_query = int(input('Введите номер месяца: '))
except ValueError:
    print('Нужно ввести номер месяца')
else:
    if user_query in winter:
        print('Зима')
    elif user_query in spring:
        print('Весна')
    elif user_query in summer:
        print('Лето')
    elif user_query in autumn:
        print('Осень')
    else:
        print('В году только 12 месяцев')

