user_query = input('Введите строку: ')
words = user_query.split()
string_number = 1
for element in words:
    print(f'{string_number}). {element[:10]}' if len(element) > 10 else f'{string_number}). {element}')
    string_number += 1
