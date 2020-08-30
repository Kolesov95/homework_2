list_count = int(input('Введите количество элементов списка: '))
my_list = []
while len(my_list) < list_count:
    my_list.append(input('Введите элемент списка: '))
print(f'Исходный список: {my_list}')
if list_count % 2 == 0:
    for number in range(0, len(my_list), 2):
        my_list[number], my_list[number+1] = my_list[number+1], my_list[number]
else:
    for number in range(0, len(my_list)-1, 2):
        my_list[number], my_list[number+1] = my_list[number+1], my_list[number]
print(f'Новый список: {my_list}')
