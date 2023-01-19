
# a = 1
# b = a
# a+=1
# b+=1
# print(id(a),id(b))



# __hash()__

# тернарный оператор
# выражение_1 если условие иначе выражение_2
# выражение_1 истина if условие else выражение_2  в противном случае
# print(5 if 1>0 else 0)




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




    def buy_house(self,discount):
        price = Small_House(8500).final_price(discount)
        if self.__money > price:
            self.make_deal(price)
            return self.__money
        return 'Not enough money'

    def make_deal(self, price):
        self.__money -= price
        self.__house = Small_House(8500)

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


# small_house = Small_House(8500)
# print(human.buy_house(small_house,5))
# print(human.earn_money(500))
print(human.earn_money(8500))
print(human.buy_house(5))
print(human.info())


# is / ==
# a = [1,2]
# b = [1,2]
# print(a == b)
# print(a is b)
# print(id(a),id(b))

