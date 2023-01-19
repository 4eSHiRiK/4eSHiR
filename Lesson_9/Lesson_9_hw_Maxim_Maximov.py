import random


#
# elem = [1,3,4,'hi',3]
#
# elem.insert(1,2)
# print(elem)
# elem[1]=3
# print(elem)


#TASK 1 Все числа этого списка проверить на чётность. Если число
# чётное, то посчитать сумму его цифр. Если нечётное, то
# заменить его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.


# def sum(element):
#     summa = 0
#     for i in str(element):
#         summa += int(i)
#     return summa
#
#
# def chet(element):
#
#
#
# list=[15,48,'hello',6,19,'world']
# for element in list:
#     if type(element) is int:
#         if element % 2 == 0:
#             print(sum(element))
#         elif element % 2 != 0:
#             index = list.index(element)
#             list[index] = 1
#             print(list)
#     elif type(element) is str:
#         glas = 0
#         s0glas = 0
#         for letter in element:
#             if letter in 'aeiouy':
#                 glas += 1
#             else:
#                 s0glas +=1
#         print(f'V {element} koli4estvo glasnih {glas} ,soglasnih {s0glas}')



#VERSION 2

# def sum(element):
#     summa = 0
#     for i in str(element):
#         summa += int(i)
#     return summa
#
# def nechet(element):
#     index = list.index(element)
#     list[index] = 1
#     return list
#
# def slovo(element):
#     glas = 0
#     s0glas = 0
#     for letter in element:
#         if letter in 'aeiouy':
#             glas += 1
#         else:
#             s0glas += 1
#     return f'V {element} kolvo glasnih {glas}, a soglasnih {s0glas}'
#
# list=[15,48,'hello',6,19,'world']
# for element in list:
#     if type(element) is int:
#         if element % 2 == 0:
#             print(sum(element))
#         elif element % 2 != 0:
#             print(nechet(element))
#     elif type(element) is str:
#         print(slovo(element))




#TASK RANDOM LIST

# lst = [random.randint(0,10) for i in range(7)]
# print(lst)
# def proverka(lst):
#     chet = 0
#     nechet = 0
#     for num in lst:
#         if num % 2 == 0:
#             chet += 1
#         else:
#             nechet += 1
#     if chet > nechet:
#         sum = 0
#         for num_1 in lst:
#             sum += num_1
#         return sum
#     else:
#         return lst[0] * lst[2] * lst[5]
# print(proverka(lst))


#VERSIA 2

# def chet(lst):
#     chet = 0
#     nechet = 0
#     for num in lst:
#         if num % 2 == 0:
#             chet += 1
#         else:
#             nechet += 1
#     return chet, nechet
#
# def sravnenie(lst):
#     result = chet(lst)
#     if result[0]>result[1]:
#         result = sum(lst)
#     else:
#         result = lst[0] * lst[2] * lst[5]
#     return result
# print(sravnenie([random.randint(0,10) for i in range(7)]))

#VERSIA 3


# def proverka(lst):
#     chet = 0
#     nechet = 0
#     for num in lst:
#         if num % 2 == 0:
#             chet += 1
#         else:
#             nechet += 1
#     if chet > nechet:
#         result = 1
#     else:
#         result = 2
#     return result
#
# def func_oper(lst):
#     proverka(lst)
#     result = proverka(lst)
#     if result == 1:
#         sum = 0
#         for num_1 in lst:
#               sum += num_1
#         return sum
#     else:
#         return lst[0] * lst[2] * lst[5]
#
#
# print(func_oper([random.randint(0,10) for i in range(7)]))


#TASK FIGURI
# def figure(fig):
#     if fig == 1:
#         rectangle()
#     if fig == 2:
#         triangle()
#     if fig == 3:
#         circle()
#
# def rectangle():
#     length = int(input('enter length'))
#     width = int(input('Enter width'))
#     print(f'Square is {lengthwidth}')
#
# def triangle():
#     side_1 = int(input('Enter first side length'))
#     side_2 = int(input('Enter second side length'))
#     side_3 = int(input('Enter third side length'))
#     p = (side_1 + side_2 + side_3)/2
#     print(f'Square is: {math.sqrt((p(p-side_1)(p-side_2)(p-side_3)))}')
#
# def circle():
#     radius = int(input('Enter radius'))
#     print (f'Square is: {math.pi*(radius**2)}')
#
# figure(int(input('Enter number figure')))


#TASK COUNT

# def count(lst):
#     new_lst = []
#     new_lst_2 = []
#     for new_num in lst:
#         if lst.count(new_num) > 1:
#             new_lst.append(new_num)
#             if new_lst.count(new_num) == 1:
#                 continue
#             else:
#                 new_lst_2.append(new_num)
#     return new_lst_2
#
# print(count([1,2,3,9,10,4,5,6,7,8,8,9,10,5,6,6]))