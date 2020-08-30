my_list = [7, 5, 3, 3, 2]
print(my_list)
user_number = int(input('Введите число: '))
for i in range(len(my_list)):
    if user_number >= my_list[i]:
        my_list.insert(i, user_number)
        break
    elif user_number <= my_list[len(my_list)-1]:
        my_list.append(user_number)
        break
print(my_list)
