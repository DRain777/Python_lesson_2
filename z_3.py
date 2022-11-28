#3) Узнайте у пользователя число n.Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
num = int(input("Введите число от 0 до 9: "))
if num == 0:# проверка введеного числа
    result = 0
    print(result)
elif num > 9:
    result_1 = "Вы ввели число больше 9"
    print(result_1)
   

else:
    num_2 = num * 10 + num
    num_3 = num_2 * 10 + num
    summa = num + num_2 + num_3
    print(f' {num} + {num_2} + {num_3} = {summa}')
    
   