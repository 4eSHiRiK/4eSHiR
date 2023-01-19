import math


# def calculator(num_1,num_2,oper):
#     while True:
#         if oper == '0':
#             print('WorkEnd program')
#             break
#         if oper == '-':
#             result = num_1-num_2
#         elif oper == '+':
#             result = num_1+num_2
#         elif oper == '/':
#             if num_2 == 0:
#                 result = 'error'
#             else:
#                 result = num_1/num_2
#         elif oper == '*':
#             result = num_1*num_2
#         return result
#
# print(calculator(float(input('Enter number 1')),float(input('enter number 2')),input('oper')))




def figure(fig):
    if fig == 1:
        rectangle()
    if fig == 2:
        triangle()
    if fig == 3:
        circle()

def rectangle():
    length = int(input('enter length'))
    width = int(input('Enter width'))
    print(f'Square is {length*width}')

def triangle():
    side_1 = int(input('Enter first side length'))
    side_2 = int(input('Enter second side length'))
    side_3 = int(input('Enter third side length'))
    p = (side_1 + side_2 + side_3)/2
    print(f'Square is: {math.sqrt((p*(p-side_1)*(p-side_2)*(p-side_3)))}')

def circle():
    radius = int(input('Enter radius'))
    print (f'Square is: {math.pi*(radius**2)}')

figure(int(input('Enter number figure')))