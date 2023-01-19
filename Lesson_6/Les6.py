

# for i in range(5,10,2):
#     print(i)

# for i in range(4):
#     print(i)


# str[4:8] -> str[start:stop]
# range(start, stop, step)

# for i in range(4,8):
#     print(i)

# for i in range(4,8,1):
#     print(i)


# for i in range(10,5,-2):
#     print(i)


# for i in 'Я учу Python':
#     print(i*2)



# for i in range(15,0,-1):
#     print(i)


#TASK 1
# str = input('Enter string')
# symbol = input('Enter symbol')
# res = " "                         #Сюда складываются значения
# for s in str:
#     if s != symbol:
#         res += s
# print(f'res {res}')


#TASK 2
# for num in range(100,1000):
#     if num % 100 == 0:
#         print(i)

# for num in range(100, 999, 100):
#     print(num)


#TASK 3

# for num in range(94, 351):         #Через for
#     if num % 5 == 0:
#         print(num)

# num = 94                           #Через while
# while num < 351:
#     if num % 5 == 0:
#         print(num)
#     num+=1

# # Списки
# list = [1, 'hello',2.0,True]
# print(len(list))
# print(list[0])
# print(list[1])
# list = ['hello']
# print(list[0])


# Функции списков
# lst = [1,2,3,4]
# lst.append(4)
# print(f'append: {lst}')
# l = lst.count(4)
# print(f'count: {l}')
# l_1 = lst.index(4)
# print(f'index: {l_1}')
# l_2 = lst.pop(4)
# print(f'pop: {l_2}')
# lst.remove(4)
# print(f'remove: {lst}')
# lst.reverse()
# print(f'reverse: {lst}')


#Добавление элемента в конец списка
# lst = ['Hello', 15, 3.14]
# lst.append(True)
# lst_2 = lst + [111]
# print(lst_2)
# print(lst)

#Вывод длинны списка
#
# arr = ['str1','str2','str3']
# print(len(arr))

# Вывод эл-тов списка на экран
# strings = ['str1','str2','str3']
# for string in strings:
#     print(string)

#BREAK
# for number in range(10):
#     if number == 5:
#         break
#     print('Number: ' + str(number))
# print('Code out of the cycle')
#
# #CONTINUE
# for number in range(5):
#     if number == 3:
#         continue
#     print('Number: ' + str(number))
# print('Code out of the cycle')

# PASS
# for n in range(5):
#     if n == 3:
#         pass
#     print(f'Number {n}')
# print('Some code out of th cycle')

# for l in "I'm python developer":   #НЕТ ПРИНТА У I'm python developer! поэтому только else выводиться на экран
#     if l == 'P':                   #ЕСЛИ маленькая p то ничего не выводит - сработал брейк
#         break
# else:
#     print('We successfully pass the cycle')

#TASK 4 Если четных больше то находим сумму, если нечетных то произведение 1 3 6 эл-тов
# lok = 0  #Четные
# ret = 0  #Нечетные
# lst = [1,2,3,4,5,6,7]
# for num in lst:
#     if num % 2 == 0:
#         lok += 1
#     else:
#         ret += 1
# if lok>ret:
#     print(f'sum all numbers {sum(lst)}')
# else:
#     print(f'Произведение 1,3,6 элементов {lst[0]*lst[2]*lst[5]}')

#TASK 5 Находим сумму и произведение
# arr = [1,2,3,10]
# sum = 0
# pr = 1
# for i in arr:
#     sum += i
#     pr *= i
# print(f'sum: {sum} and proizvedenie: {pr}')


# Вложенный цикл
# for x in range(10,510,100):                    #строки 1,2,3,4 - внешний цикл
#     for y in range(10,51,10):                  #строки 2,3 - вложенный цикл
#         print(x+y)                             #строки 2,3,4 - тело внешнего цикла
#     print('You are the best')                  #строка 3 - тело вложенного цикла
# print('Oi boi')

# res=1
# for num in range(1,10):
#     for num_1 in range(1,10):
#         print(num*num_1, '', end=' ')
#     print()


# ТВОРЧЕСКОЕ ЗАДАНИЕ
# Задачи с for переделать на while и наоборот
# И списки
