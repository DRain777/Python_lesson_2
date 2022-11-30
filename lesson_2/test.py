my_list = input("Введите 7 элементов списка через пробел: ").split()
i = len(my_list)
if i != 7:
    print(f'{i}  вы не ввели 7 элементов')
else:    
    my_list[0],my_list[1] = my_list[1],my_list[0]
    my_list[2],my_list[3] = my_list[3],my_list[2]
    my_list[4],my_list[5] = my_list[5],my_list[4]
   

print(my_list)