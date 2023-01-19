import random


# print(5==5) #Если правильное то True
# print('hello'==5) # Если нет то False
#
# print(5!=5) # Если правильно то пишет False
# print('hello'!=5) # Если нет то True
#
#
# print(6>5) #Больше или меньше
# print(6<5)
#
#
# print(6>=5) #Больше/меньше или равно
# print(6<=5)
# print(6<=6)
#
# a = 5
# if a>3:             #Условие если выполняется идет в блок если нет, то не входит и идет дальше по коду
#     a += 1
#     print('hello')
#     print(a)
# else:
#
    # print(1000)
# a = 5
# if  a:             # a != 0
#     a += 1
#     print('hello')
#     print(a)
# else:
#     print(1000)


# if True:        #True = 1, False = 0
#     print('world')
# if False:
#     print('world')

# a = 5
# if a>10:
#     print('a>10')
# else:
#     print('a<10')


# TASK 1 Проверяет четное или нечетное число
# number = int(input('Enter your number'))
# if number%2==0:
#     print('4etnoe')
# else:
#     print('Ne4etnoe')




# a = 5   # Elif дает возможность нескольких if

# if a%2==0:
#     print('1')
# elif a == 5:
#     print('2')
# else:
#     print('3')


# a = 5
# if a-2==0:
#     print('1')
# elif a == 5:     # Срабатывает скрипт
#     print('2')
# elif type(a) == int:
#     print('3')
# else:
#     print('4')
# print('999')


#TASK 2
# finger = int(input('Enter code of finger'))
# if finger == 1:
#     print('right misinec')
# elif finger == 2:
#     print('right be3imen')
# elif finger == 3:
#     print('right fuck')
# elif finger == 4:
#     print('right yka3')
# elif finger == 5:
#     print('right bigbrother')
# elif finger == 6:
#     print('left mizinec')
# elif finger == 7:
#     print('left be3imen')
# elif finger == 8:
#     print('left fuck')
# elif finger == 9:
#     print('left yka3')
# elif finger == 10:
#     print('left bigbrother')
# else:
#     print('Net palcev')


# TASK 3
# month = int(input('Enter number of month (1-12)'))
# if month >= 3 and month <= 5:
#     print('spring')
# elif month >= 6 and month <= 8:
#     print('summer')
# elif month >= 9 and month <= 11:
#     print('autumn')
# else:
#     print ('winter')
#
# month_1 = int(input('Enter number of month (1-12)'))
# if 3<=month_1<6:
#     print('spring')
# elif 6<=month_1<9:
#     print('summer')
# elif 9<=month_1<12:
#     print('autumn')
# elif month_1 == 12:
#     print('winter')
# elif 1<=month_1<3:
#     print('winter')
#
# month_1 = int(input('Enter number of month (1-12)'))
# if 3<=month_1<6:
#     print('spring')
# elif 6<=month_1<9:
#     print('summer')
# elif 9<=month_1<12:
#     print('autumn')
# else:
#     print('winter')

# a = 5
# b = 2
# if a ==5 and b == 1:
#     print('true')
# print('hi')

# if a == 5 or b == 1:
#     print('true')
# print('hi')


# if not b:
#     print('false')
# print('390')

# a = 1
# b = 2
# c = True
#
# if a>0 and b<0:
#     print('and')
# elif a>0 or b <0:
#     print('or')
#
# if not c == False:
#     print('not')



#TASK 4

# num_1 = int(input('Enter number 1'))
# num_2 = int(input('Enter number 2'))
# num_3 = int(input('Enter number 3'))
#
# if num_1>num_2 and num_1>num_3:
#     print(f"{num_1} the biggest one")
# elif num_2>num_3:
#     print(f'{num_2} the biggest one')
# else:
#     print(f"{num_3} the biggest one")

# a = 1
# b = 2
# c = 3
# if a>b and a>c:
#     print('naibolshee', a)
# else:
#     if b>c:
#         print('naibolshee', b)
#     else:
#         print('naibolshee', c)

#TASK 5
# import random
#
# rock = 0        #Можно не применять цифры а сразу сравнивать числа через скобки (ПРИМЕР НИЖЕ)
# scissors = 1
# paper = 2
# user = int(input('rock - 0, scissors - 1, paper - 2'))
# comp = random.randint(0,2)
# print(comp)
# if user == comp:
#     print('draw')
# elif user==rock and comp==scissors:
#     print('win user')
# elif user==scissors and comp==paper:
#     print('win user')
# elif user==paper and comp==rock:
#     print('win user')
# else:
#     print('comp win')
#
#
# c = random.randint(1,3)
# h = int(input('enter number 1(stone), 2(scis), 3(papper)'))
# if c==h:
#     print('draw')
# elif (c==1 and h == 2) or (c == 2 and b == 3) or (c == 3 and h == 1):
#     print('win human')
# else:
#     print('comp win')

# a = 5
# b = 4
# if not a == b:
#     print('WTF')
# #TASK 6
# x = 1
# y = 2
# two_val = (x<y)
# if two_val:
#     print('true')
# else:
#     print("false")

#TASK 7




#TASK 8



#Предикаты
# i = int(input())
# is_digit = (type(i)==int)
# print(is_digit)

# string = input('enter string')
# if (string == 'Mister'):
#     print('is_mister')
