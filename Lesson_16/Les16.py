
# for e,i in enumerate([1,2,3,4], 1):
#     print(e,i)

#TASK 1
# Напишите функцию, которая в качестве аргументов будет принимать
# рост и вес. Функция должна возвращать индекс массы тела.
# # В зависимости от полученного BMI, интерпретируйте полученный
# индекс.
# # Прим:
# # 25 >= BMI < 30
# # >>> Вы имеете избыточный вес

# height = int(input('Enter your height in cm'))
# weight = int(input('Enter your weight in kg'))
# def heal(height,weight):
#     bmi = weight/(height**2)
#     if bmi < 16:
#         return 'You have severe underweight'
#     elif 16<bmi<18.5:
#         return 'You have insufficient (deficit) body weight'
#     elif 18.5<bmi<25:
#         return 'You have normal weight'
#     elif 25<bmi<30:
#         return 'You have overweight (preobesity)'
#     elif 30<bmi<35:
#         return 'You have obesity 1 degree'
#     elif 35<bmi<40:
#         return 'You have obesity 2 degree'
#     else:
#         return 'You have obesity 3 degree'
# print(heal(height,weight))


#TASK 2
# Напишите функцию, определяющую вид фигуры по количеству
# переданных в качестве аргумента сторон. Функция должна вернуть
# строку, представляющую собой вид фигуры
# Программа должна корректно обрабатывать
# и выводить названия
# для фигур с количеством сторон от трех до десяти включительно.
# Если введенное пользователем значение находится за границами
# этого диапазона, уведомите его об этом.

# def figure(*args):
#     if len(args) == 3:
#         return "You choose triangle"
#     elif len(args) == 4:
#         return "You choose rectangle"
#     elif len(args) == 5:
#         return "You choose pentagon"
#     elif len(args) == 6:
#         return "You choose hexagon"
#     elif len(args) == 7:
#         return "You choose heptagon"
#     elif len(args) == 8:
#         return "You choose octagon"
#     elif len(args) == 9:
#         return "You choose enneagon"
#     elif len(args) == 10:
#         return "You choose decagon"
#     else:
#         return "You enter numbers of side out of range"
# print(figure(*(input('Enter values'))))


# def figure(side):
#     if side == 3:
#         return "You choose triangle"
#     elif side == 4:
#         return "You choose rectangle"
#     elif side == 5:
#         return "You choose pentagon"
#     elif side == 6:
#         return "You choose hexagon"
#     elif side == 7:
#         return "You choose heptagon"
#     elif side == 8:
#         return "You choose octagon"
#     elif side == 9:
#         return "You choose enneagon"
#     elif side == 10:
#         return "You choose decagon"
#     else:
#         return "You enter numbers of side out of range"
# print(figure(int(input('Enter number of sides'))))



#TASK 3
# Напишите функцию, принимающую на вход дату и выводящую на экран дату,
# следующую за ней.
# Например: если пользователь введет дату, соответствующую 18 ноября 2019
# года, на экран должен быть выведен следующий день, то есть 19 ноября 2019
# года. Если входная дата будет представлять 30 ноября, то на выходе мы должны
# получить 1 декабря.
# И наконец, если ввести последний день года – 31 декабря 2019-го, пользователь
# должен увидеть на экране дату 1 января 2020-го. Дату пользователь должен
# вводить в три этапа: год, месяц и день.


# def calendar(year):
#     year = year
#     month = int(input('Enter month name'))
#     day = int(input('Enter number of day'))
#     if day == 31 and month == 12:
#         year = year+1
#         day = 1
#         month = 1
#     else:
#         if month == (1 or 3 or 5 or 7 or 8 or 10) and day == 31:
#             month = month+1
#             day = 1
#         elif month == (4 or 6 or 9 or 11) and day == 30:
#             month = month+1
#             day = 1
#         elif month == 2 and day == 28:
#             month == month+1
#             day = 1
#         elif month == 12 and day == 31:
#             month == 1
#             day = 1
#         else:
#             day = day+1
#     return f'{year}:{month}:{day}'
#
# print(calendar(int(input('Enter year'))))


# from datetime import datetime,timedelta
# def next_day(w):
#     dt = datetime.strptime(w,'%Y-%m-%d')
#     res = dt + timedelta(days=1)
#     return res.strftime('%Y-%m-%d')
# print(next_day('2020-02-29'))


#TASK 4

# Интернет-магазин предоставляет услугу экспресс-доставки для части
# своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# последующие.
# Напишите функцию, принимающую в качестве единственного
# параметра количество товаров в заказе и возвращающую общую
# сумму доставки.
# В основной программе должны производиться запрос количества
# позиций в заказе у пользователя и отображаться на экране сумма
# доставки.


# def shop(items):
#     total_sum = 10.95+(2.95*(items-1))
#     return total_sum
#
# print(shop(int(input('Enter number of items you wanna buy'))))


#TASK 5
# Напишите функцию, принимающую на вход два целочисленных параметра,
# представляющих числитель и знаменатель дроби.
# В теле функции должно выполняться максимально возможное сокращение
# дроби, а полученные в итоге числитель и знаменатель должны быть возвращены
# исходной программе.
# Например, если на вход функции передать числа 6 и 63 числитель и
# знаменатель итоговой дроби должны быть 2 и 21.
# В основной программе нужно запросить у пользователя числитель и
# знаменатель исходной дроби, передать их в функцию и вывести на экран
# результат.


# def drob(up,down):
#     while up % 2 == 0 and down % 2 == 0:
#         up = up/2
#         down = down/2
#     while up % 3 == 0 and down % 3 == 0:
#         up = up/3
#         down = down/3
#     while up % 4 == 0 and down % 4 == 0:
#         up = up / 4
#         down = down / 4
#     while up % 5 == 0 and down % 5 == 0:
#         up = up / 5
#         down = down / 5
#
#     return f'{up}/{down}'
#
# print(drob(int(input('Enter numerator')),int(input('Enter denominator'))))

# def drob(up,down):
#     div = up
#     while div != 0:
#         if up % div ==0 and down % div == 0:
#             up /= div
#             down /= div
#             return f'{up}/{down}'
#     else:
#         div -= 1
#
# print(drob(int(input('Enter numerator')),int(input('Enter denominator'))))


#TASK 6

# Напишите функцию, которая в качестве аргумента будет принимать список
# размером не менее 10 элементов. Список должен включать строки и числа.
# Функция должна вывести:
# 1. Список в перевернутом виде
# 2. Список в порядке убывания
# 3. Список в порядке возрастания
# 4. Срез списка от 2 до 7 элемента
# 5. Список с удаленным 5 элементом
# 6. Список без дубликатов


# def lst(lst):
#     print(lst[::-1])
#     print(sorted([C],reverse=True))
#     print(sorted([i for i in lst if isinstance(i,str)],key=len,reverse=True))
#     print(lst[1:7])
#     lst.pop(4)
#     print(lst)
#     print(list(set(lst)))
#


# lst([1,2,3,4,'pribet','hi',67,'wow'])


#TASK 7
# В стандартной библиотеке языка Python присутствует функция count, позволяющая
# подсчитать, сколько раз определенное значение встречается в списке.
# Напишите новую функцию countRange, которая будет подсчитывать количество
# элементов в списке, значения которых больше или равны заданному минимальному
# порогу и меньше максимального.
# Функция должна принимать три параметра: список, минимальную границу и
# максимальную границу.
# Возвращать она будет целочисленное значение, большее или равное нулю.
# В основной программе реализуйте демонстрацию вашей функции для нескольких
# списков с разными минимальными и максимальными границами. Удостоверьтесь, что
# программа будет корректно работать со списками, содержащими как целочисленные
# значения, так и числа с плавающей запятой


# def countRange(lst,min,max):
#     count_elem = 0
#     for elem in lst:
#         if min<=elem<max:
#                 count_elem += 1
#     return count_elem
#
#
#
# print(countRange([1,2,3.5,3.2,2.9,5,7,8],0,3))


#TASK 8
# Напишите функцию, которая в качестве аргумента будет принимать
# список.
# Функция должна возвращать количество всех подсписков внутри
# переданного списка.

# def lst(lst):
#     podspisok = 0
#     for elem in lst:
#         if type(elem) is list:
#             podspisok +=1
#     return podspisok
#
# print(lst([1,2,[1,2,3],[23,4]]))


#TASK 9
#
# Анаграммами называются слова, образованные путем взаимной
# перестановки букв. В английском языке, например, анаграммами
# являются слова
# «live» и «evil», а в русском – «выбор» и «обрыв».
# Напишите программу, которая будет запрашивать у пользователя два
# слова, определять, являются ли они анаграммами, и выводить на
# экран ответ


# def anagrama(word_1,word_2):
#     lst_word_1 = list(word_1)
#     lst_word_2 = list(word_2)
#     if len(lst_word_2) == len(lst_word_1):
#         for elem in lst_word_1:
#             if elem in lst_word_2:
#                 continue
#             else:
#                 return 'This words are not anagramma'
#                 break
#         for elem_1 in lst_word_2:
#             if elem_1 in lst_word_1:
#                 continue
#             else:
#                 return 'This words are not anagramma'
#                 break
#         return 'This words are anagramma'
#     else:
#         return 'This words are not anagramma'
#
#
# print(anagrama(input('enter word 1'),input('enter word 2')))

# def anagrams(str_1,str_2):
#     return sorted(str_1) == sorted(str_2)
# print(anagrams('live','evil'))


#TASK 10

# dict_phone = {1:['.',',','?','!',':'],
#                   2:['a','b','c'],
#                   3:['d','e','f'],
#                   4:['g','h','i'],
#                   5:['j','k','l'],
#                   6:['m','n','o'],
#                   7:['p','q','r','s'],
#                   8:['t','u','v'],
#                   9:['w','x','y','z'],
#                   0:[' ']}
#
# text = input('Enter your text')
# code_text = ''
# for elem in text.lower():
#     for key,res in dict_phone.items():
#         if elem in res:
#             code_text += str(key)*(dict_phone[key].index(elem)+1)
# print(code_text)

#TASK 11


def rekurs(lst):
    if lst == []:
        return lst
    elif isinstance(lst[0], list):
        lst1 = lst[0]
        lst2 = lst[1:]
        return rekurs(lst1) + rekurs(lst2)
    elif not isinstance(lst[0], list):
        lst1 = lst[:1]
        lst2 = lst[1:]
        return lst1 + rekurs(lst2)
print(rekurs([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
print(rekurs([]))