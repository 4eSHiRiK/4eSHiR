import math
import random

#Про ПРИНТЫ
# a = 5
# b = 6
#
# print(f"1) Здесь мы сложим {a} + {b}")
# print("2) Здесь мы сложим {} + {}".format(a,b))
# print("3) Здесь мы сложим %d + %d" %(a,b))
# print("4) Здесь мы сложим " + str(a) + ' + ' + str(b))
# print("5) Здесь мы сложим", a, '+', b)
#
# print(f"1) Здесь мы сложим {a} + {b} и получим {a+b}")
# print("5) Здесь мы сложим", a, '+', b,  'и получим', a+b)
# print("2) Здесь мы сложим {} + {} и получим {}".format(a,b,a+b))
# print("3) Здесь мы сложим %d + %d и получим %d" %(a,b,a+b))
#
# adress = 'minsk'
# house_number = 34
# c = f'{adress} {house_number}'
# print(c)
#
# # += /= #для добавления цифр, строк... к переменной
#
# #координаты
# lat = 1.1
# lon = 0.2
# geo = '{1}, {0}' .format(lat, lon) #можно менять индексы переменных в формате
# geo1 = '{0}, {1}' .format(lat, lon)
# print(geo)
# print(geo1)


# a = 7
# b = 5
# c = a+b #сложение
# f = a-b #вычитание
# g = a/b #деление истинное
# m = a*b # умножение
# d = a**b # возведение в степень
# h = a//b # деление до целого числа
# t = a%b # вывод остатка после деления
# print(c, f, g, m, d, h, t)

# a = 'Hello'
# print(a[1]) #для вывода индекса в строке

#TASK 1
# a = 4
# b = 10
# c = 3
# # d = (a+b)/c
# # print(d)
# # f = a**c/c
# # print(f)
# g = b//c+4
# print(g)
# t = b%c/a
# print(t)
# print(f"{5}+{5}")

# TASK 2
# age = int(input('Age'))
# number = int(input('Number'))
# N_1 = int (input('Quality'))
# N_2 = int (input('Speed'))
# result = age/number*N_1+N_2
# print(result)
# age = int(input('Age'))
# number = int(input('Number'))
# N_1 = int (input('Quality'))
# N_2 = int (input('Speed'))
# word = age+number/N_1*N_2
# print(word)
# age = int(input('Age'))
# number = int(input('Number'))
# N_1 = int (input('Quality'))
# N_2 = int (input('Speed'))
# c = int(input('dsad'))
# revers = age%number+N_1/N_2*c
# print(revers)
# age = int(input('Age'))
# number = int(input('Number'))
# N_1 = int (input('Quality'))
# N_2 = int (input('Speed'))
# ux = (age+number)-N_1*N_2
# print(ux)
# age = int(input('Age'))
# number = int(input('Number'))
# N_1 = int (input('Quality'))
# N_2 = int (input('Speed'))
# c = int(input('dsad'))
# uf = age/number%N_1*N_2**c
# print(uf)


# d = 17/2*3+2
# print(d)
#
# print(17/2*3+2)


# TASK 3
# money = 11
# bread = 1.5
# quantity = 3
# wallet = money-quantity*bread
# print(wallet)
# # print(money-quantity*bread)
# ut = money%wallet
# print(ut)

# TASK 4
# d = [20,21,22,23,24,25,26,27,28,29,30]
# a = ((d[0]+d[1]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9])/10)
# print(a)
# b = 4
# c = math.sqrt(b)
# print(c)

# Task 5
# gradus = float(input('write gradus'))
# print(math.radians(gradus))
#
# gradus1 = float(input('gradus')) * math.pi / 180
# print(gradus1)
#
# gradus2 = float(input('gradus')) * 3.14 / 180
# print(gradus2)\


# TASK 6

# print(f"Значение дискриминанта равно {float(input('write a'))**2-4*float(input('write b'))*float(input('write c'))}")
# print (f'ghdbtn {5+5} fdsf')
# print("Значение дискриинанта равно", float(input('write a'))**2-4*float(input('write b'))*float(input('write c')))


# TASK 7
# print(f"Square is {float(input('write h'))*float(input('write hyp'))/2} and perimetr is {2*float(input('catet'))+float(input('hyp'))}")


# TASK 8
# n = str(random.randint(100, 999))
# n1 = int(n[0])
# n2 = int(n[1])
# n3 = int(n[2])
# n4 = n1+n2+n3
# print(n4)
# n = (random.randint(100, 999))
# n11 = n // 100
# n21 = (n//10) % 10
# n31 = n % 10
# print(n11+n21+n31)