import random



#Ввод значений в цикле

# password = ''
#
# while password != 'password':
#     print('What is the password?')
#     password = input('')
# print('Yes, the password is' + password + '.You may enter')


# Использование команды Continue

# number = 0
# while number < 10:
#     number += 1
#     if number %2 == 0:
#         continue
#     print(number)


# #TASK 4
# Пользователь вводит два числа c клавиатуры, необходимо
# вывести на экран все отрицательные числа, лежащие между
# ними. Например пользователь ввел -5 и 3, на экране вывелось
# -4, -3, -2, -1

# num_1 = int(input('Enter first number'))
# num_2 = int(input('Enter second number'))
# if (num_1 == 0 and num_2 == 0) or (num_1 == 0 and num_2 >=0) or (num_2 == 0 and num_1 >=0) or (num_1 > 0 and num_2 > 0):
#     print('Enter negative number')
# if num_1 < 0 and num_2 > 0:
#     while num_1<0:
#         num_1 += 1
#         if num_1 == 0:
#             break
#         print(num_1)
# if num_2 < 0 and num_1 > 0:
#     while num_2<0:
#         num_2 += 1
#         if num_2 == 0:
#             break
#         print(num_2)
# if num_1 <= num_2 < 0:
#     while num_1 < num_2:
#         num_1 += 1
#         if num_1 == num_2:
#             break
#         print(num_1)
# if num_2 <= num_1 < 0:
#     while num_2 < num_1:
#         num_2 += 1
#         if num_2 == num_1:
#             break
#         print(num_2)


# Просто еще немного циклов

# do = True
# while do:
#     print('Do smth before do')
#     do = False
#     print('Do smth after do')
# else:
#     print('The end')


# while do:
#     print('Do smth before do')
#     break
#     do = False
#     print('Do smth after do')
# else:
#     print('The end')
#
#
# while do:
#     print('Do smth before do')
#     do = False
#     continue
#     print('Do smth after do')
# else:
#     print('The end')



# TASK 5
# Напишите программу, которая считывает числа до тех пор, пока не встретит
# отрицательное число. При появлении отрицательного числа программа
# должна завершиться.

# num_user = int(input('Enter your number'))
# while num_user != 0:
#     if num_user < 0:
#         print(f'Your number {num_user} is negative')
#         break
#     num_user = int(input('Enter next number'))
# else:
#     print('negative number is not entered')



# TASK 6 CALCULATOR
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную
# операцию).

# num_1 = float(input('Enter number 1: '))            #Решение через if
# oper =input('enter oper')
# num_2 = float(input('Enter number 2: '))
#
# if oper == '-':
#     print(num_1-num_2)
# if oper == '+':
#     print(num_1+num_2)
# if oper == '/':
#     if num_2 == 0:
#         print('error')
#     else:
   #         print(num_1/num_2)
# if oper == '*':
#     print(num_1*num_2)


# num_1 = float(input('Enter first number'))              #Через цикл
# num_2 = float(input('Enter second number'))
# while True:
#     oper = input('oper')
#     if oper == '0':
#         break
#     elif oper == '+':
#         print(num_1+num_2)
#     elif oper == '-':
#         print(num_1-num_2)
#     elif oper == '*':
#         print(num_1*num_2)
#     elif oper == '/':
#         if num_2 != 0:
#             print(num_1/num_2)
#         else:
#             print('Error')





# TASK CASINO
# Казино.
# Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета (1 красный,
# 2 черный).
# Пользователю дается 5 попыток угадать номер и цвет
# (Прим. введения с клавиатуры: 3 красный). В случае неудачи
# вывести на экран правильную комбинацию.


num_user = int(input('Enter 1 - 10 number'))  #Пользователь вводит число
color_user = input('color')                   #Пользователь вводит цвет
tr = 0                                        #Счетчик попыток
num_comp = random.randint(1,10)               #Казино машина чисел
color_comp = random.randint(1,2)              #Казино машина цвета ниже условия когда человек проигрывает
while (num_comp != num_user) or (color_user == 'red' and color_comp == 2) or (color_user == 'black' and color_comp == 1):
    tr += 1                                   # увеличение попытки на 1
    print('Not that time')                    # Оповещение о неудачи
    if tr == 5:                               # Превышение лимита попыток
        if color_comp == 1:                   # Преобразование числа цвета в текст
            color_comp = 'red'
        else:
            color_comp = 'black'
        print(f'You lose, right combination is {num_comp} {color_comp}') # Проигрыш
        break                                                            # Выход из цикла в случае победы
    num_user = int(input('Enter 1 - 10 number'))                         # Повторный ввод числа
    color_user = input('color')                                          # Повторный ввод цвета
else:
    print('You win')





# num_user = int(input('Enter 1 - 10 number'))
# color_user = input('color')
# tr = 0
# num_comp = random.randint(1,10)
# color_comp = random.randint(1,2)
# print(color_comp, num_comp)
# if color_comp == 1:
#     color_comp = 'red'
# else:
#     color_comp = 'black'
# while (num_comp != num_user) or (color_user != color_comp):
#     tr += 1
#     print('Not that time')                                                      #red - 1 black - 2
#     if tr == 5:
#         print(f'You lose, right combination is {num_comp} {color_comp}')
#         break
#     num_user = int(input('Enter 1 - 10 number'))
#     color_user = input('color')
# else:
#     print('You win')
