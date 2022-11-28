#2) Пользователь вводит время в секундах. Переведите время в часы,
#  минуты и секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк. 
seconds = int(input( 'введите время в секундах:'))
minuts = seconds // 60
seconds %= 60 
hours = minuts // 60
minuts %= 60
if hours > 99:
    print('Слишком большое значения для формата чч:мм:сс')
else:
    hours_10 = hours // 10
    hors_1 = hours % 10
    minuts_10 = minuts // 10      
    minuts_1 = minuts % 10
    second_10 = seconds // 10    
    second_1 = seconds % 10
    print(f'{hours_10}{ hors_1}:{minuts_10}{minuts_1}\:{second_10}{second_1}')  
         