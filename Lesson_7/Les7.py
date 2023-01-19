import math
import random

#TASK 1
# katet_1 = int(input('Enter long katet1'))
# katet_2 = int(input('Enter long katet2'))
# print(f'Hyp = {math.sqrt(katet_1**2+katet_2**2)}')


#TASK 2


# num_1 = int(input('Enter number 1'))
# num_2 = int(input('Enter number 2'))
# num_3 = int(input('Enter number 3'))
# if num_1<num_2<num_3 or num_1>num_2>num_3:
#     print(f'Srednee is {num_2}')
# elif num_2<num_1<num_3 or num_2>num_1>num_3:
#     print(f'Srednee is {num_1}')
# elif num_1 == num_2 or num_2 ==num_3 or num_3 == num_1:
#     print('You enter equal numbers')
# else:
#     print(f'Srednee is {num_3}')



#TASK 3

# num_1 = random.randint(0,100000)
# num_2 = random.randint(0,100000)
# # if (num_1 % 2 == 0 and num_2 % 2 != 0):
# #     print(num_2)
# # elif (num_1 % 2 != 0 and num_2 %2 ==0):
# #     print(num_1)
# # else:
# #     print('error')
# a=0
# lst = [num_1,num_2]
# for i in lst:
#     if i % 2 != 0 and a == 0:
#         print(i)
#         a+=1


#TASK 4

# a = str(int(input('Enter code')))
# print(a[::-1])

# a = int(input('Enter code'))
# i=0
# while a > 0:
#     i = i*10 + a % 10
#     a = a//10
# print(i)



#TASK 5

# s = 'hello my world'
# s1 = s.split(' ')
# print(len(s1))



#TASK 6

# s = '   djg asdfj   klahrt  ni '
# l = s.split()
# s1 = '*'.join(l)
# print(s1)
#
# s = input()
#
# i = 0
# while s[i] == ' ':
#     i += 1
# s = s[i:]
#
# i = len(s)
# while s[i - 1] == ' ':
#     i -= 1
# s = s[:i]
#
# s_new = s[0]
# i = 1
# while i < len(s):
#     if s[i] != ' ':
#         s_new += s[i]
#     elif s[i - 1] != ' ':
#         s_new += ''
#     i += 1
# print(s_new + '!')

# TASK 9
# #
# str = input('Enter string')
# # print(str.lower())
#
# x=''
# for i in range(len(str)):
#     if str[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         x = x + str[i]
# print(x)

# for i in str:
#     if i.islower():
#         x+=i
# print(x)

# TASK 10


# lst = []
# for i in range(101):
#     if i % 7 == 0:
#         continue
#     else:
#         lst += [i]
# print(lst)
#
# for i in range(101):
#     if i % 7 == 0:
#         continue
#     print(i)



#TASK 11
# sum = 0
# for i in range(101):
#     sum+=i
# print(sum)



#TASK 12

# num = int(input('Enter your number'))
# # i = 1
# # pr = 1
# # while i <= num:
# #     pr = pr*i
# #     i+=1
# # print(pr)
#
# pr = 1
# for i in range(1,num+1):
#     # if i !=0:
#         pr *= i
# print(pr)


#TASK 14

# N = int(input('Enter number'))
# i = 2
# s = []
# while i<N:
#     i = i**2
#     if i > N:
#         break
#     s +=[i]
# print(s)
# #
#
# a = 1
# b = 2
# a,b=b,a


#TASK 15

# a = int(input('Enter number'))
# b = int(input('Enter number'))
# c = int(input('Enter number'))
# decr = b**2 - 4 * a * c
# if decr > 0:
#     x1 = (-b + math.sqrt(decr))/(2*a)
#     x2 = (-b - math.sqrt(decr)/(2*a)
#     print(x1,x2)
# elif decr == 0:
#     x1 = (-b/2*a)
#     print(x1)
# else:
#     print('Net kornei')



#TASK 16
# b = []
# a = ['he', 2, True, 2,"2"]
# for l in a:
#     if a.count(l) < 2:
#         b+= [l]
# print(b)

# for elem in a:
#     if elem in b:
#         continue
#     b.append(elem)
# print(b)


#TASK 17

# lst_1 = [1,2,2, True, 'he',]
# lst_2 = [5,2,2, False, 'he']
# lst_3 = []
# for i in lst_1:
#     if i in lst_2:
#         lst_3 += [i]
# print(lst_3)
#
# for i in lst_1:
#     for i1 in lst_2:
#         if i == i1:
#             lst_3.append(i)
# print(lst_3)

# for elem_1 in lst_1:
#     if elem_1 in lst_3:
#         continue
#     for elem_2 in lst_2:
#         if elem_1 == elem_2:
#             lst_3.append(elem_1)
#             break
# print(lst_3)
