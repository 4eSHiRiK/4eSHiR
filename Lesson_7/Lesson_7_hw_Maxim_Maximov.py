import math
import random





#TASK 1 Перемножить все нечётные значения в диапазоне от 1 до 30
# pr = 1
# for num in range(1,31,2):
#     pr *= num
# print(pr)
#
# numbers = 1
# pr_1 = 1
# while numbers <= 30:
#     if numbers % 2 != 0:
#         pr_1 *= numbers
#     numbers += 1
# print(pr_1)

#TASK 2 Записать в массив все числа в диапазоне от 1 до 100 кратные 5

# lst = []
# for num in range (1,101):
#     if num % 5 == 0:
#         lst.append(num)
# print(lst)
#
# lst_1 = []
# numbers = 1
# while numbers <= 100:
#     if numbers % 5 == 0:
#         lst_1.append(numbers)
#     numbers += 1
# print(lst_1)


#TASK 3   Вывести на экран все чётные значения в диапазоне от 1 до 71.


# for num in range(1,71,2):
#     num += 1
#     print(num)

# number = 1
# while number <=71:
#     if number % 2 == 0:
#         print(number)
#     number += 1


#TASK 4 Дан массив чисел. Если число встречается более двух раз, то добавить
# его в новый массив.

# lst = [1,2,3,4,5,2,2,4]
# new_lst = []
# new_lst_2 = []
# for num in lst:
#     if lst.count(num) > 1:
#         new_lst.append(num)
#         if new_lst.count(num) == 1:
#             continue
#         else:
#             new_lst_2.append(num)
# print(new_lst_2)



#TASK 1 По двум введенным пользователем катетам вычислить длину
# гипотенузы.

# katet_1 = int(input('Enter first katet length'))
# katet_2 = int(input('Enter second katet length'))
# print(f'Hyp is: {math.sqrt((katet_1**2)+(katet_2**2))} ')



#TASK 2 Вводятся три разных числа. Найти, какое из них является
# средним (больше одного, но меньше другого).

# num_1 = int(input('Enter first number'))
# num_2 = int(input('Enter second number'))
# num_3 = int(input('Enter third number'))
# if num_1<num_2<num_3 or num_1>num_2>num_3:
#     print(f'srednee is {num_2}')
# elif num_2<num_1<num_3 or num_2>num_1>num_3:
#     print('Srednee is ', num_1)
# else:
#     print("srednee is {}".format(num_3))


#TASK 3 Из двух случайных чисел, одно из которых четное, а другое
# нечетное, определить и вывести на экран нечетное число.

# num_1 = random.randint(1,100)
# num_2 = random.randint(1,100)
# print(num_1,num_2)
# if num_1 % 2 == 0 and num_2 % 2 != 0:
#     print(f'ne4etnoe is {num_2}')
# elif num_1 % 2 != 0 and num_2 % 2 == 0:
#     print('ne4etnoe is %d'%(num_1))
# elif num_1 % 2 != 0 and num_2 % 2 !=0:
#     print('{} and {} are ne4etnie'.format(num_1,num_2))
# else:
#     print('Ne4etnih 4icel net')


#TASK 4 Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

# code = str(int(input('Enter code')))
# print(code[::-1])
#
# code_2 = int(input('Enter your code'))
# back_code = ''
# while code_2 > 0:
#     back_code += str(code_2 % 10)
#     code_2 = code_2 //10
# print(back_code)



#TASK 5 Найти площади прямоугольника, треугольника или круга.
# примечание: надо ввести фигуру 1-прямоугольник, 2-треугольник,
# 3-круг.
#
# figure = int(input('Enter name of figure 1 - rectangle, 2 - triangle, 3 - circle'))
# if figure == 1:
#     length = int(input('enter length'))
#     width = int(input('Enter width'))
#     print(f'Square is {length*width}')
# elif figure == 2:
#     side_1 = int(input('Enter first side length'))
#     side_2 = int(input('Enter second side length'))
#     side_3 = int(input('Enter third side length'))
#     p = (side_1 + side_2 + side_3)/2
#     print(f'Square is: {math.sqrt((p*(p-side_1)*(p-side_2)*(p-side_3)))}')
# else:
#     radius = int(input('Enter radius'))
#     print(f'Square is: {math.pi*(radius**2)}')




#TASK 6 Определить существование треугольника по трем сторонам
# Примечание: У треугольника сумма любых двух сторон должна
# быть больше третьей. Иначе две стороны просто "лягут" на третью
# и треугольника не получится.



# count = 0
# while count == 0:
#     side_1 = int(input('Enter first side length'))
#     side_2 = int(input('Enter second side length'))
#     side_3 = int(input('Enter third side length'))
#     if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2+side_3>side_1:
#         print('It is a real triangle')
#         count += 1
#     else:
#         print('This triangle is unreal, enter right sides')



#TASK 7 Принадлежит ли точка кругу
# Примечание: Если выбрать точку на координатной плоскости,
# то можно увидеть, что проекции ее координат на оси x и y
# являются катетами прямоугольного треугольника. А гипотенуза
# этого прямоугольного треугольника как раз показывает
# расстояние от начала координат до точки. Таким образом, если
# длина гипотенузы будет меньше радиуса круга, то точка будет
# принадлежать кругу; иначе она будет находится за его
# пределами.

# radius = int(input('enter circle radius '))
# x_point, y_point = int(input('enter X coordinate')), int(input('enter Y coordinate'))
# if radius >= math.sqrt((x_point**2)+(y_point**2)):
#     print('Point is in circle')
# else:
#     print('Point is out of circle')

#TASK 8 Вводится строка, состоящая из слов, разделенных пробелами.
# Требуется посчитать количество слов в ней.

# string = input('Enter string')
# words = string.split()
# print(len(words))

#TASK 9 Введите строку c клавиатуры, которая состоит из букв разных
# регистров. Нужно очистить эту строку от всех заглавных букв и
# вывести результат на экран.

# new_str = ''
# string = input('Enter string')
# for letter in string:
#     if letter.islower():
#         new_str += letter
# print(new_str)


#TASK 10 Написать программу, которая выводит числа от 0 до 100 на экран,
# пропуская числа кратные 7

# for num in range(101):
#     if num % 7 == 0:
#         continue
#     print(num)




#TASK 11 Найти сумму ряда чисел от 1 до 100. Полученный результат
# вывести на экран

# sum = 0
# for num in range(1,101):
#     sum += num
# print(sum)

#TASK 12
# По данному натуральному n вычислите значение n!.

# num = int(input('Enter your number'))
# agent = 1
# pr = 1
# while agent <= num:                     # Через while
#     pr *= agent
#     agent += 1
# print(pr)
#
# num_2 = int(input('Enter your number'))     # Через for
# pr_1 = 1
# for agent_2 in range(1,num_2+1):
#     pr_1*= agent_2
# print(pr_1)


#TASK 13 Пользователь передает целое положительное число N,
# выведете на экран последовательность от 1 до N "ёлочкой",
# например для N=17

#
# tree = int(input('Enter number'))
# agent = 1
# while agent != tree - 1:
#     if agent == 1:
#         print(agent)
#     elif agent == 2:
#         print(agent,agent+1)
#     elif agent == 4:
#         print(agent,agent+1,agent+2)
#     elif agent == 7:
#         print(agent,agent+1,agent+2,agent+3)
#     elif agent == 11:
#         print(agent,agent+1,agent+2,agent+3,agent+4)
#     agent+=1
# print(tree-1,tree)


# tree = int(input('Enter number'))
# agent = 1
# agent_row = 0
# row = 1
# while agent <= tree:
#     print(agent,end=' ')
#     agent+=1
#     agent_row+=1
#     if agent_row == row:
#         print()
#         row+=1
#         agent_row=0

tree = int(input('Enter number'))
agent = 1
agent_row = 0
row = 1
string = ''
while agent <= tree:
    while agent_row != row and agent<=tree:
        agent_row+=1
        string += str(agent)
        string += ' '
        agent += 1
    print(string)
    row+=1
    agent_row = 0
    string = ''







#TASK 14Найти пересечения в 2 списках и записать в 3 список эти
# пересечения

# lst_1 = [1,2,3,4,4,'hi']
# lst_2 = [1,4,6,7,4,'hi']
# lst_3 = []
# for vir in lst_1:
#     if vir in lst_3:
#         continue
#     for vir_2 in lst_2:
#         if vir == vir_2:
#             lst_3.append(vir)
# print(lst_3)


#TASK 15 Есть список с фамилиями. Пользователь вводит фамилию. Если фамилия есть в списке, то она удаляется, если нет,
# то такой фамилии нет.

# #
# surname_lst = ['Maximov','Krish', 'Sobolev']
# surname_user = input('Enter surname')
# # for check in surname_lst:
# #     if surname_user == check:
# #         surname_lst.remove(check)
# #         break
# # else:
# #     print('This surname is not identify')
# # print(surname_lst)
#

# surname_lst = ['Maximov','Krish', 'Sobolev']
# surname_user = input('Enter surname')
# if surname_user in surname_lst:
#     surname_lst.remove(surname_user)
# else:
#     print('This surname is not identify')
# print(surname_lst)