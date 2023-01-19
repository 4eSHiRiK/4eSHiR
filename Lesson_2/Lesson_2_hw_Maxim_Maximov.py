import math
import random

# TASK 1

# apples_Ann = 2
# apples_Pol = 5
# print(f"Pol has {apples_Pol} apples, and Ann has {apples_Ann} apples.")


# TASK 2

# long_cube = float(input('Enter cube length'))
# print(f"Cube volume is {math.pow(long_cube, 3)}.")
# print(f'Cube side surface is {long_cube**2*6}.')


# TASK 3
# tree_length = 20
# speed_snail = 2
# backflip = 1
# day_progress = speed_snail - backflip
# print(f"{tree_length/day_progress-1*backflip}")
# days = 0
# result_snail = 0
# while tree_length > result_snail:
#     result_snail += 2
#     days += 1
#     if tree_length == result_snail:
#         break
#     result_snail -= 1
# print(days)

# TASK 4 Количество чистых денег после учета подоходного налога
# sallary = float(input('Enter your sallary'))
# tax = 13
# print(f"You will get {sallary - sallary*tax/100} money")

#TASK 5

# cells = float(input('Enter number of cells, mln'))
# weight_reactor = float(input('Enter weight of reactor, kg'))
# coefficient = 0.3
# virus_activity = 1*10**8
# print(f"Volume of virus liquid is {cells*1000000*weight_reactor*coefficient/virus_activity} littres")

# TASK 6

test_number = random.randint(0,99)
test_number2 = random.randint(10, 99)
test_number3 = random.randint(90, 99)

print(f"{test_number, test_number2, test_number3}")
print(f"{test_number-test_number2}")
print(f'{math.fmod(test_number, test_number2)} and {math.pow(test_number, test_number2)}')
print(f"{test_number/test_number2/math.fmod(test_number3, test_number)} ")






