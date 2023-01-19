# # a = 5
# # print(type(a))
# # pi = 3.14
# # print(type(pi))
# # s = "Hello, world"
# # print(type(s))
# # t = True #for test
# # print(type(t))
# #
# #
# # # n = int(input('введите число'))
# # # m = n+1
# # # print (m)
# #
# # p = input ('Hello')
# # i = p+'1'
# # print (i)
#
#
# # age = int(input ('Text your age'))
# # product = int(input('Numbers of product'))
# # comment = (input('Left your comment'))
# # money = float(input('enter your sum of money'))
# # print(comment, age, product)
# # print(money)
#
#
# cat = int(4)
# dog = float(3.14)
# ret = str('fdgfdg')
# gfr = bool(True)
#
# cat1 = 4
# dog1 = 3.14
# ret1 = 'fdgfdg'
# gfr1 = True
#
# cat2 = str(cat)
# dog2 = str(dog)
#
#
# # name = input('Введите имя')
# # surname = input('Введите фамилию')
# # secondName = input('Введите отчество')
# # age1 = int(input('Возраст'))
# # city = input('Ваш город')
# # print(name, surname, secondName)
# # print(age1)
# # print(city)
#



class Tomato:
    states = ['Проростание', 'Зачатки цветов', 'Зелёный плод', 'Бурый плод']

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        self._state = self.states[self.states.index(self._state) + 1]

    def is_ripe(self):
        if self._state == self.states[-1]:
            pass


class TomatoBush(Tomato):
    def __init__(self, amount, index):
        super().__init__(index)
        self.amount = amount
        self.tomatoes = [num for num in range(1, amount+1)]
        self.flag = False

    def grow_all(self):
        for tomato in self.tomatoes:
            self._state[tomato] = self.states[self.states.index(self._state) + 1]

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if self._state[tomato] == self.states[-1]:
                self.flag = True
            else:
                self.flag = False
                break
        if self.flag is not False:
            return True

    def give_away_all(self):
        for ripe in self.tomatoes:
            if self._state[ripe] == self.states[-1]:
                self.tomatoes.remove(ripe)
