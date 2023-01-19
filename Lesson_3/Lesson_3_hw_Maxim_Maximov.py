import random


#TASK Snail
# tree_length = 20
# speed_snail = 2
# backflip = 1
# day_progress = speed_snail - backflip
# print(f"{tree_length/day_progress-1*backflip}") #Подгонометрия как у Оли только с вычитанием последней ночи(backflip)
#
# tree_length = 20  #Скорее всего я шиз, но она работает так же подгонометрией, просто больше if.
# speed_snail = 4
# backflip = 1
# days = 0
# result_snail = 0
# if tree_length == result_snail:
#     print(f"Snail reach top of tree in {days}.")
# else:
#     result_snail += speed_snail
#     days += 1
#     if tree_length == result_snail:
#         print(f"Snail reach top of tree in {days}.")
#     else:
#         result_snail -= backflip
#         result_snail += speed_snail
#         days += 1
#         if tree_length == result_snail:
#             print(f"Snail reach top of tree in {days}.")
#         else:
#             result_snail -= backflip
#             result_snail += speed_snail
#             days += 1
#             if tree_length == result_snail:
#                 print(f"Snail reach top of tree in {days}.")
#             else:
#                 result_snail -= backflip
#                 result_snail += speed_snail
#                 days += 1
#                 if tree_length == result_snail:
#                     print('Snail reach top of tree in', days)
#                 else:
#                     result_snail -= backflip
#                     result_snail += result_snail
#                     days += 1
#                     if tree_length <= result_snail:
#                         print('Да ладно, и зачем улитке ползти на дерево в 19 метров?/nОна сумасшедшая?/n За', days, 'дней')
#                     else:
#                         print('Надеюсь она не сорвется вниз')


# #TASK 6 - Bool True and False
# human_num1 = int(input('Enter number'))
# human_num2 = int(input('Enter second number'))
# result = human_num1 > human_num2
# result_2 = human_num1 == human_num2
# if result == True:
#     print('First man win')
# elif not result_2 == False:
#         print('OMG IT IS DRAW')
# else:
#     print('Second man win')


#TASK 7 - Triangle
# side_1 = float(input('Enter first side size'))
# side_2 = float(input('Enter second side size'))
# side_3 = float(input('Enter third side size'))
# if side_1+side_2>side_3 and side_1+side_3>side_2 and side_2+side_3>side_1:
#     print('Take your triangle')
# else:
#     print('It cannot be')


#TASK 8 - Calculator

#TEST не рабочий, но я разобрался как починить!
num_1 = float(input('Enter your number'))
oper = input('+,-,/,*')                   #
num_2 = float(input('Enter your next number'))
result = str(num_1) + oper + str(num_2)
if result == str(num_1) + '+' + str(num_2):
    print(f'{num_1+num_2}')
elif result == str(num_1) + '-' + str(num_2):
    print(f'{num_1-num_2}')
elif result == str(num_1) + '/' + str(num_2):
    print(f'{num_1/num_2}')
elif result == str(num_1) + '*' + str(num_2):
    print(f'{num_1*num_2}')
else:
    print('Incorrect operation')

#Рабочий вариант
# num_1 = float(input('Enter your number')) #Я попытался через преобразование в чисел в строку, но тогда он не считал
# oper = input('+,-,/,*')                   #их значения ибо они были в типе str
# num_2 = float(input('Enter your next number'))
# result = "num_1" + oper + "num_2"
# if result == "num_1" + '+' + "num_2":
#     print(f'{num_1+num_2}')
# elif result == "num_1" + '-' + "num_2":
#     print(f'{num_1-num_2}')
# elif result == "num_1" + '/' + "num_2":
#     print(f'{num_1/num_2}')
# elif result == "num_1" + '*' + "num_2":
#     print(f'{num_1*num_2}')
# else:
#     print('Incorrect operation')

#TASK 8 NEXT TRY
# num_1 = int(input('Enter your number'))
# oper = input("oper")
# num_2 = int(input('Enter your next number'))
# if oper == "+":
#     print(f'{num_1+num_2}')
# elif oper == "-":
#     print(f'{num_1-num_2}')
# elif oper == "/":
#     print(f'{num_1/num_2}')
# elif oper == "*":
#     print(f'{num_1*num_2}')
# else:
#     print('Incorrect operation')


#TASK 9 - PREDICAT


# string = input('enter string')
# is_string = (string == 'Mister')
# print(is_string)

#TASK 10 - PickHero
# armor = input('Choose color of your armor')
# shield = input('Choose color of your shield')
# is_armor = (armor == 'yellow')
# is_armor = (armor == 'black')
# is_shield = (shield == 'black')
# print(is_armor)
# print(is_shield)


# armor = input('Choose color of your armor')
# shield = input('Choose color of your shield')
# is_armor = (armor == 'yellow' or armor == 'black')
# is_shield = (shield == 'black')
# print(is_armor)
# print(is_shield)

# armor = input('Choose color of your armor')
# shield = input('Choose color of your shield')
# is_warrior = (armor != 'red' and shield == "black")
# print(is_warrior)

#TASK 1.1
# num_1 = int(input('Enter number 0-9')) #Совпадение числа пользователя и компа
# num_comp = random.randint(0,9)
# print(num_comp)
# if num_1 != num_comp:
#     print('You lose')
# else:
#     print('you win')

#TASK 1.2                                 #Просим ввести пользователя 3 цифры и если совпадут - приз!
# num_1 = int(input('Enter number 0-9'))
# num_2 = int(input('Enter number 0-9'))
# num_3 = int(input('Enter number 0-9'))
# num_comp = random.randint(100,999)
# print(num_comp)
# if num_1 == num_comp//100:
#     print('Совпадение первой цифры')
# if num_2 == num_comp//10%10:
#     print('Ого, вы отгадали и вторую, остался 1 шаг до победы')
# if num_3 == num_comp%10:
#     print('А вы везунчик, вам явно нужно сегодня идти в казино')
# else:
#     print('Вы проиграли, не расстраивайтесь')

#TASK 2

# day = int(input('Enter your birth day'))
# month = int(input('Enter your birth month'))
# if (21 <= day <= 31 and month == 3) or (day <= 20 and month == 4):
#     print(f'Aries')
# elif (21 <= day <= 30 and month == 4) or (day <= 21 and month == 5):
#     print(f'Taurus')
# elif (22 <= day <= 31 and month == 5) or (day <= 21 and month == 6):
#     print(f'Gemini')
# elif (22 <= day <= 30 and month == 6) or (day <= 22 and month == 7):
#     print(f'Cancer')
# elif (23 <= day <= 31 and month == 7) or (day <= 21 and month == 8):
#     print(f'Leo')
# elif (22 <= day <= 31 and month == 8) or (day <= 23 and month == 9):
#     print(f'Virgo')
# elif (24 <= day <= 30 and month == 9) or (day <= 23 and month == 10):
#     print(f'Libra')
# elif (24 <= day <= 31 and month == 10) or (day <= 22 and month == 11):
#     print(f'Scorpio')
# elif (23 <= day <= 30 and month == 11) or (day <= 22 and month == 12):
#     print(f'Sagittarius')
# elif (23 <= day <= 31 and month == 12) or (day <= 20 and month == 1):
#     print(f'Capricorn')
# elif (21 <= day <= 31 and month == 1) or (day <= 19 and month == 2):
#     print(f'Aquarius')
# elif (20 <= day <= 28 and month == 2) or (day <= 20 and month == 3):
#     print(f'Pisces')
# else:
#     print(f'Incorrect date')


