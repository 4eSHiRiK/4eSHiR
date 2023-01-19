import math
import random

# Пример функции

# def func():
#     print('Hello ! I\'m func')
#     return 'Hello ! I\'m func'
# func()
# print(func())


#TASK 1 Simple func
# def sum():
#     s = 0
#     lst = [1, 2, 3, 4, 5, 6]
#     for num in lst:
#         s += num
#     print(f'{s}')
# sum()

#TASK 2 func with arguments

# def lite_sum(a,b):
#     print(a+b)
#
# lite_sum("1",'2')


# def lite_sum_2(a,b):
#     c = a+b
#     return c
#
# print(lite_sum_2('1','2'))
#
#
# a = 1
# b = 2
# print(a+b)
#
# print(lite_sum_2(5,10))


#
# def l_sum(a,b,d):
#     c = (a+b)*d
#     return c
#
# print(l_sum(d=5,b=10,a=100))
#
# sum = l_sum(4,1,2)
# print(sum)

# def func_1():
#     a = 1
#     b = 2
#     return a+b
# a = func_1()
#
# def func_2():
#     a
#     c=3
#     return a+c
#
#
# print(func_1())
# print(func_2())


# def func_1():
#     global a
#     a = 1
#     b = 2
#     return a+b
#
#
# def func_2():
#     c=3
#     return a+c
#
# print(func_1())
# print(func_2())
#
# print(a*1000)
#
# def simple_func_sum(a,b): return a+b
#
#
# print(simple_func_sum(int(input('Enter num')),2))

# def sum_simple_func(a,b):
#     return a+b
# print(sum_simple_func(1,2))
#
# s = lambda a, b: a + b
# print(s(1,2))



# p = lambda x = 2 , y = 3: x**y
# print(p())
#
# def stepen(x,y): return x**y
# print(stepen(2,3))
#
# def stepen(x=2,y=3): return x**y
# print(stepen())


#TASK 2 Visocosnii god
# def is_year_leap(year):
#     year = int(input('Enter number of the year'))
#     if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
#         return 'Visocosnii'
#     else:
#         return 'Ne visocosnii'
# print(is_year_leap(2000))

# def is_year_leap(year):
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         return 'Visocosnii'
#     else:
#         return 'Ne visocosnii'
# print(is_year_leap(int(input('Enter number of the year'))))

# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 == 0 and year % 400 == 0
# print(is_year_leap(int(input('Enter number of the year'))))


#TASK 3
# def square_1(side):
#     return f'Perimetr is {side * 4} Square is {side * side} Diagonal is {math.sqrt((side ** 2) + (side ** 2))}'
# print(square_1(int(input('Enter side size'))))


#TASK 4


# def season(month):
#     if 3 <= month < 6:
#         return 'spring'
#     elif 6<=month<9:
#         return 'summer'
#     elif 9<=month<12:
#         return 'autumn'
#     elif month == 12 or 1<=month<3:
#         return 'winter'
# print(season(int(input('enter month number'))))

# def season(month):
#     if 3 <= month < 6:
#         name = 'spring'
#     elif 6<=month<9:
#         name = 'summer'
#     elif 9<=month<12:
#         name = 'autumn'
#     elif month == 12 or 1<=month<3:
#         name = 'winter'
#     return name
# print(season(int(input('enter month number'))))


#TASK 5

# def is_prime(number):
#     print(number)
#     d = 2
#     while number % d != 0:
#         d+=1
#     return d == number
#
# print(is_prime(11))



#TASK 6

# def srednee(lst):
#     srednee_arif = 0
#     for num in lst:
#         srednee_arif += num
#     return srednee_arif/len(lst)
#
#
# # lst=[1,2,3,4,5,6,7,8,9,10]
# print(srednee([1,2,3,4,5,6,7,8,9,10]))


# def avg_func(lst,n):
#     s = 0
#     for i in range(n):
#         s += lst[i]
#     return s/n
#
# print(avg_func([1,2,3],3))



#Чтобы сделать список рандомный
# N = 10
# my_lst = [0]*10
# for i in range(N):
#     my_lst[i]=random.randint(1,100)
#
# def avg_func_1(my_lst):
#     s = 0
#     for i in range(N):
#         s += my_lst[i]
#     return s/N
# print(my_lst)
# print(avg_func_1(my_lst))