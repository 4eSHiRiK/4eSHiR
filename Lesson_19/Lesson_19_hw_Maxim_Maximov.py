


# class Tomato:
#
#     states = {0:'незрелый',1:'полузрелый',2:'зрелый'}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     def grow(self):
#         self._state += 1
#         return f'My tomato is {Tomato.states.get(self._state)}'
#
#     def is_ripe(self):
#         if self._state == 2:
#             return True
#         return False
#
#
# class TomatoBush:
#
#     def __init__(self, num):
#         self.tomatoes = [Tomato(i) for i in range(num)]
#
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def give_away_all(self):
#         # self.tomatoes.clear()
#         self.tomatoes = []
#         print(self.tomatoes)
#
#
#     def all_are_ripe(self):
#         for i in self.tomatoes:
#             if i.is_ripe():
#                 self.give_away_all()
#                 return True
#             return False
#
#
#
# class Gardener:
#
#     def __init__(self,name,plant):
#         self.name = name
#         self._plant = plant
#
#
#     def work(self):
#         print('gardener working')
#         self._plant.grow_all()
#         print('grow on next stage')
#
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             return f'Tomato is ready'
#         return f'Tomato is not ready'
#
#
#     @staticmethod
#     def knowledge_base():
#         return f'Help for gardener'
#
#
# print(Gardener.knowledge_base())
#
# tomato_bush = TomatoBush(3)
# gardener = Gardener('Maxim', tomato_bush)
#
# print(gardener.work())
# print(gardener.harvest())
# print(gardener.work())
# print(gardener.harvest())





class Human:

    default_name = 'Maxim'
    default_age = 22

    def __init__(self):
        self.name = self.default_name
        self.age = self.default_age
        self.__money = 0
        self.__house = None


    def info(self):
        return f'Name - {self.name} \n' \
               f'Age - {self.age} \n' \
               f'Money - {self.__money} \n' \
               f'House - {self.__house} '


    @staticmethod
    def default_info():
        return f'{Human.default_name}'\
               f'{Human.default_age}'


    def earn_money(self, salary):
        self.__money += salary




    def buy_house(self,house,discount):
        price = house.final_price(discount)
        if self.__money > price:
            self.make_deal(house,price)
            return self.__money
        return 'Not enough money'

    def make_deal(self,house,price):
        self.__money -= price
        self.__house = house

# print(Human.default_info())

human = Human()
# print(human.info())
# print(human.earn_money(100))
# print(human.info())


class House:

    def __init__(self,area,price):
        self._area = area
        self.price = price

    def final_price(self,discount):
        final_price = self.price - (self.price*discount/100)
        return final_price

class Small_House(House):

    default_area = 40

    def __init__(self,price):
        super().__init__(Small_House.default_area,price)


small_house = Small_House(8500)
# print(human.buy_house(small_house,5))
# print(human.earn_money(500))
print(human.earn_money(8500))
print(human.buy_house(small_house,5))
print(human.info())
