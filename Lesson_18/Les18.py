#
#
#
# # class Car:
# #
# #     def __str__(self):
# #         return 'Car is object'
# #
# #     def start(self):
# #         print('Engine is ready')
# #
# #
# # car = Car()
# # print(car.start())
# # print(car.__str__())
# # print(car)
#
# # class Phone:
# #
# #     def __init__(self,color,model):
# #         self.color = color
# #         self.model = model
# #
# #
# #     @classmethod
# #     def toy_phone(cls,color):
# #         toy_phone = cls(color,'Toy_phone',None)
# #         return toy_phone
# #
# #     def check_sim(self,mobile_operator):
# #         if self.model == 'I785' and mobile_operator == 'MTS':
# #             print('My operator is MTS')
# #
# #     @staticmethod
# #     def model_hash(model):
# #         if model == 'I785':
# #             return 34565
# #         elif model == 'K498':
# #             return 45567
# #         else:
# #             return None
# #
# # print(Phone.toy_phone('red'))
# # print(Phone.model_hash('I785'))
# # my_phone = Phone('red','I785')
# # my_phone.check_sim('MTS')
#
#
#
# # Класс Human
# #
# # 1. Создайте класс Human.
# # 2. Определите для него два статических поля: default_name и default_age.
# # 3. Создайте метод init(), который помимо self принимает еще два параметра: name и
# # age. Для этих параметров задайте значения по умолчанию, используя свойства
# # default_name и default_age. В методе init() определите четыре свойства:
# # публичные - name и age. Приватные - money и house.
# # 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и
# # money.
# # 5. Реализуйте справочный статический метод default_info(), который будет выводить
# # статические поля default_name и default_age.
# # 6. Реализуйте метод earn_money(), увеличивающий значение свойства money.
#
# # class Human:
# #
# #     default_name = 'Maxim'
# #     default_age = 22
# #
# #     def __init__(self,house,money):
# #         self.name = self.default_name
# #         self.age = self.default_age
# #         self.house = house
# #         self.money = money
# #
# #     def info(self):
# #         return self.name, self.age, self.house,self.money
# #
# #     def default_info(self):
# #         return self.default_name , self.default_age
# #
# #     def earn_money(self):
# #         return self.money*self.money
# #
# # h = Human('house',5000)
# # print(h.info())
# # print(h.default_info())
# # print(h.earn_money())
#
# # class Human_1:
# #         default_name = 'Maxim'
# #         default_age = 22
# #
# #         def __init__(self,name=default_name,age=default_age):
# #             self.name = name
# #             self.age = age
# #             self.__house = 'House'
# #             self.__money = 5000
# #
# #         def info(self):
# #             return self.name, self.age, self.__house,self.__money
# #
# #         @staticmethod
# #         def default_info():
# #             return Human_1.default_name , Human_1.default_age
# #
# #         def earn_money(self, salary):
# #             self.__money += salary
# #             return self.__money
# #
# # print(Human_1.default_info())
# # h = Human_1()
# # print(h.info())
# # print(h.earn_money(500))
#
# #Parents class
# # class Phone:
# #
# #     def __init__(self):
# #         self.is_on = False
# #
# #     """пользовательский метод. Вкл. телефон"""
# #     def turn_on(self):
# #         self.is_on = True
# #
# #     """пользовательский метод. Звонит телефон, если он включен"""
# #     def call(self):
# #         if self.is_on:
# #             return f"Calling..."
# #
# # #Son class
# # class MobilePhone(Phone):
# #
# #     #add new attribute in init
# #     def __init__(self):
# #         super().__init__()
# #         self.battery = 0
# #
# #     """пользовательский метод. Зарядим телефон на переданное значение"""
# #     def charge(self,num):
# #         self.battery += num
# #         return f"We're charging battery up to {num}. All battery = {self.battery} "
# #
# # my_mobile_phone = MobilePhone()
# # print(dir(my_mobile_phone))
#
# #
# # class Camera:
# #     def camera(self):
# #         pass
# #
# # class Radio:
# #     def radio(self):
# #         pass
# #
# # class Phone(Radio,Camera):
# #     def phone(self):
# #         pass
# #
# # print(Phone().__dir__())
#
#
# # class House:
# #
# #     def __init__(self,area,price):
# #         self._area = area
# #         self._price = price
# #
# #
# #     def final_price(self,discount):
# #         total = self._price - (self._price * (discount/100))
# #         return total
# #
# #
# # class SmallHouse(House):
# #
# #     st_area = 40
# #
# #     def __init__(self,price):
# #         super().__init__(SmallHouse.st_area,price)
# #
# #     def area(self):
# #         return f"{self._area} sq.metres"
# #
#
#
# # class Car:
# #
# #     def __init__(self,model):
# #         self.model = model
# #
# #     @property
# #     def model(self):
# #         return self.__model
# #
# #     @model.setter
# #     def model(self,model):
# #         if model < 2000:
# #             self.__model = 2000
# #         elif model > 2018:
# #             self.__model = 2018
# #         else:
# #             self.__model = model
# #
# #     def carGetModel(self):
# #         return self.model
# #
# # car_1 = Car(2019)
# # print(car_1.carGetModel())
#
# import string
# class Alphabet:
#
#     def __init__(self,lang,letters):
#         self.lang = lang
#         self.letters = letters
#         self.letter_count = 0
#
#     def print(self):
#         return self.letters
#
#     def letters_num(self):
#         return len(self.letters)
#         # for elem in self.letters:
#         #     self.letter_count += 1
#         # return self.letter_count
#
# class EngLetters(Alphabet):
#
#     __letter_num = 26
#
#     def __init__(self):
#         super().__init__('EN',string.ascii_uppercase)
#
#
#     def is_en_letter(self,letter):
#         if letter in self.letters:
#             return f'{letter} in EN Alhabet'
#
#     def letters_num(self):
#         return EngLetters.__letter_num
#
#     @staticmethod
#     def example():
#         return f'Hello'
#
# eng_alphabet = EngLetters()
# print(eng_alphabet.print())
# print((eng_alphabet.letters_num()))
# print(eng_alphabet.is_en_letter('Q'))
# print(eng_alphabet.is_en_letter('Щ'))
# print(EngLetters.example())


