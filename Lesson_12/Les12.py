import math
import random

# arr = [1,2,3]
# tuple_c = (arr,arr.reverse())
#
# print(tuple_c.count([1,2,3]))

# def func(a,b):
#     res = a+b
#     return res
# print(func(1,2))


#
# def func(c,a=3,b=4):
#     res = a+b + c
#     return res
# print(func(1))



# def factorial(n):
#     if n!=1:
#         return n * factorial(n-1)
#     else:
#         return 1
# print(factorial(3))
#
# def func(c,a=3,b=4):
#     res = a+b + c
#     return res
#
# sum_res = func(1)
#
# # print(sum_res)
# ar = sum_res
# # print(ar)
# ar_2 = func
# print(ar_2(1))

#
# def mul(a):
#     def helper(b):
#         return a+b
#     return helper
# print(mul(2)(10))



# def mul(a):
#     def helper(b):
#         return a*b
#     return helper
#
# three_mul = mul(3)
# print(three_mul(5))


# def chet(*args):
#     sum = []
#     for i in args:
#         if i % 2 == 0:
#             sum.append(f'Chetnoe {i}')
#     return sum
#
# print(chet(1,2,3,4))


# def chet(n):
#     sum = 0
#     for i in range(n):
#         if i % 2 == 0:
#             sum += 1
#     return f'chetnih {sum}'
# print(chet(4))


#
# def figure(a):
#     if a == 'circle':
#         r = int(input('Enter radius'))
#         return circle(r)
#     elif a == 'rectangle':
#         b = int(input('Enter side1'))
#         c = int(input('Enter side2'))
#         return rectangle(b,c)
#     elif a == 'triangle':
#         int(input('Enter side1'))
#         int(input('Enter side2'))
#         int(input('Enter side3'))
#         return triangle(d,f,e)
#
# def circle(r):
#     return math.pi * r ** 2
#
#
# def rectangle(b,c):
#     return b * c
#
# def triangle(*args):
#     p = (a + b + c)/2
#     return math.sqrt(p*(p-a)*(p-b)*(p-c))
#
# print(figure(input('Enter name of figure')))



# def ran(start,end):
#     lst = [random.randint(start,end) for i in range(10)]
#     return lst
# print(ran(int(input('Enter start')),int(input('Enter end'))))
# print(random())

# total = ran(int(input('Enter start')),int(input('Enter end')))
# print(total)

# N = 10
# my_list = [0]*N
# def arr(start,stop):
#     for i in range(N):
#         my_list[i] = random.randint(start,stop)
#
# arr(int(input('Enter start')),int(input('Enter end')))
# print(my_list)



# def sec(secund):
#     cek = secund % 60
#     min = secund // 60
#     if min > 60:
#         hours = min // 60
#         min = min - hours*60
#         if hours > 24:
#             days = hours // 24
#             hours = hours - days*24
#     return f'Vremeni ushlo {days} days, {hours} hours, {min} minutes, {cek} sekund'
# print(sec(int(input('Enter number of seconds'))))

# def time_conv(sec):
#     day = sec // (24*3600)
#     sec = sec % (24 * 3600)
#     hour = sec //3600
#     sec = sec % 3600
#     min = sec // 60
#     sec = sec * 60
#     return f"{day}:{hour}:{min}:{sec}"
# print(time_conv())



# def stroka(str):
#     soglasnii = 0
#     glasnii = 0
#     for i in str:
#         if i not in 'aeiouy':
#             soglasnii += 1
#         else:
#             glasnii += 1
#     return f'Kol-vo soglasnih {soglasnii}, a glasnih {glasnii}'
#
# print(stroka(input('Enter string')))



# def crazy(number):
    # return number + int(str(str(number)+str(number))) + int(str(str(number)+str(number)+str(number)))
    # return number + int(str(number)*2) + int(str(number)*3)


# print(crazy(int(input('Enter number'))))


# def pizdec(x):
#     if -5<=x<=5:
#         return x**2
#     elif x<-5:
#         return 2*(x*-1)-1
#     elif x > 5:
#         return 2*x
# for x in range(-10,11):
#     print(pizdec(x))
# # print(pizdec(x))

lst = []
for xx in range(-10,11):
    lst.append(xx)
print(lst)
def pizdec(lst):
    for x in lst:
        if -5<=x<=5:
            res = x**2
        elif x<-5:
            res = 2*(x*-1)-1
        elif x > 5:
            res = 2*x
        print(res)

print(pizdec(lst))
# print(pizdec(x))