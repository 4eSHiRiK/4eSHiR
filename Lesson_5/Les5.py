import math




# i = 0
# while i<10:
#     print(i)
#     i += 1


# i1 = 0
# while i1 < 10:
#     print(i1)
#     if i1 == 5:
#         break
#     i1 += 1
#

#Посчитать сумму чисел от 1 до 50 включительно
# a = 1
# sum = 0
# while a<=50:
#
#     sum = a + sum
#     a = a + 1
# print(sum)


#TASK 1 вывести квадраты целых чисел от 1 до 10
# a = 1
# while a<=10:
#     print(a**2)
#     print("-" * 50)
#     print(a*a)
#     print("-" * 50)
#     print(math.pow(a, 2))
#     print("-" * 50)
#     a = a + 1

#перемножить все четные значения от 0 до 125
# a = 1
# res = 1
# while a <= 125:
#     if a % 2 == 0:
#         res = res * a
#     a += 1
# print(res)


#Вывести числа от 1 до 15 в порядке убывания
# a = 15
# while a != 0:
#     print(a)
#     a-= 1




#TASK 4

# num_1 = int(input('Enter first number'))
# num_2 = int(input('Enter second number'))
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

#
# num_1 = int(input('Enter first number'))
# num_2 = int(input('Enter second number'))
# while num_1 < num_2:
#     num_1 += 1
#     if num_1 == 0:
#         break
#     print(num_1)



# for i in range(3):
#     print(i)
# else:
#     print('end')



# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print('we end')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('we have break')


#TASK 6

num_1 = float(input('Enter number 1: '))
oper =input('enter oper')
num_2 = float(input('Enter number 2: '))

if oper == '-':
    print(num_1-num_2)
if oper == '+':
    print(num_1+num_2)
if oper == '/':
    if num_2 == 0:
        print('error')
    else:
        print(num_1/num_2)
if oper == '*':
    print(num_1*num_2)

# a = int(input())
# b = int(input())
# c = input()
# while True:
#     if c == '/' and b != 0:
#         print(a/b)
#         break
#     else:
#         print("error")
#         break


