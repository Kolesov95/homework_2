quantity = int(input('Введите количество товаров: '))
my_list = []
names = []
prices = []
amount = []
units = []

number = 1
while number <= quantity:
    my_dict = {'Название': input('Введите название товара: '),
               'Цена': input('Введите цену: '),
               'Количество': input('Введите количество: '),
               'ед': input('Введите единицу измерения: ')
               }
    if my_dict['Название'] not in names:
        names.append(my_dict['Название'])
    if my_dict['Цена'] not in prices:
        prices.append(my_dict['Цена'])
    if my_dict['Количество'] not in amount:
        amount.append(my_dict['Количество'])
    if my_dict['ед'] not in units:
        units.append(my_dict['ед'])
    characteristic = (number, my_dict)
    my_list.append(characteristic)
    number += 1
for i in my_list:
    print(i)

analytics = {'Название:': names,
             'Цена:': prices,
             'Количество:': amount,
             'ед:': units}
for items in analytics.items():
    print(items)

