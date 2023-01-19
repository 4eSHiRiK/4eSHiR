





# class House:
#     """this is some dock""" #documentation
#     def build(self):
#         pass
#
#     def destroy(self):
#         pass
#
# house_item = House()
# print(dir(House))


# class Phone:
#
#     def_color = 'red'
#     def_model = 'F100'   #STATIC
#
#     def turn(self):
#         pass
#
# class My_Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model    #DYNAMIC
#
#
# class Example:
#     # global st_1,st_2
#     st_1 = 10
#     st_2 = 54
#     def __init__(self,dyn_1,dyn_2):
#         self.dyn_1 = dyn_1
#         self.dyn_2 = dyn_2
#
#     def peremen(self):
#         pr = int(input('Enter number'))
#         print(pr)
#         self.pr_1 = int(input('Enter number'))
#         print(self.pr_1)
#
#     def sum(self):
#         # return st_1 + st_2
#         return self.st_1 + self.st_2
#
#     def pow(self):
#         return self.dyn_1**self.dyn_2
#
# example = Example(3,4)
# print(example.dyn_1)
# print(example.dyn_2)
# example.peremen()
# print(example.sum())
# print(example.pow())
#


class Calculator:

    # def add_values(self):
    #     self.num_1 = int(input('Enter first number')
    #     self.num_2 = int(input('Enter second number')

    def __init__(self,num_1,num_2):
        # self.add_values()
        self.num_1 = num_1
        self.num_2 = num_2

    def minus(self):
        return self.num_1 - self.num_2
    def plus(self):
        return self.num_1 + self.num_2
    def divide(self):
        try:
            res = self.num_1/self.num_2
            return res
        except ZeroDivisionError:
            return  'cant divide on zero'

    def pow(self):
        return self.num_1 * self.num_2

calc = Calculator(int(input('Enter first number')),int(input('Enter second number')))

while True:
    oper = input('Enter oper')
    if oper == 'stop':
        break
    elif oper == '-':
        print(calc.minus())
    elif oper == '+':
        print(calc.plus())
    elif oper == '/':
        print(calc.divide())
    elif oper == '*':
        print(calc.pow())
