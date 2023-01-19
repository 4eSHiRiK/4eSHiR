# class Tomato:
#     states = ['germination','appearance of the first true leaf','overgrowth of above ground mass and roots',
#               'bud formation','bloom','fruit formation and ripening']
#
#
#
#     def __init__(self,index,state=states[0]):
#          self._index = index
#          self._state = state
#
#     def grow(self):
#         self._state = self.states[self.states.index(self._state)+1]
#         return f'The name of stage is: {self._state}'
#
#     def is_ripe(self):
#         if self._state == 'fruit formation and ripening':
#             return 'Tomato is ready'
#         else:
#             return 'Tomato is not ready'
#
#
# # tomat = Tomato(input())
# # print(tomat.grow())
# # print(tomat.is_ripe())
#
# class TomatoBush(Tomato):
# #
# #
#     def __init__(self,number,index):
#         super().__init__(index)
#         self.number = number
#         self.tomatoes = [i for i in range(1,self.number+1)]
#
#
#     # def print(self):
#     #     return self.number , self.tomatoes
#
#     #
#     def grow_all(self):
#         for veg in self.tomatoes:
#             self._state[veg] = self.states[self.states.index(self._state)+1]
#
#
# # tomat = Tomato(input())
# tomat_2 = TomatoBush(int(input('Enter number of tomatoes')),1)
# #
# # print(tomat_2.print())
# print(tomat_2.grow_all())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# Черновик
class Tomato:
    states = {1: 'germination', 2: 'appearance of the first true leaf', 3: 'overgrowth of above ground mass and roots',
              4: 'bud formation', 5: 'bloom', 6: 'fruit formation and ripening'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self.change_state()
        # self._state = self.states.get(self._index+1)
        # return f'The name of stage is: {self._index}'

    def is_ripe(self):
        if self._state == 6:
            return 'Tomato is ready'
        return 'Tomato is not ready'

    def change_state(self):
        if self._state < 6:
            self._state += 1
        self.print_info()

    def print_info(self):
        return f" tomat {self._index} is {Tomato.states[self._state]}"


# tomat = Tomato(3)
# print(tomat.grow())
# print(tomat.is_ripe())
# print(tomat.print_info())

class TomatoBush(Tomato):

    def __init__(self, number, index):
        super().__init__(index)
        self.tomatoes = [Tomato(i) for i in range(number)]
#
    def print_ii(self):
        return self.tomatoes
#
#     #
    def grow_all(self):
        for veg in self.tomatoes:
            veg.grow()


# tomat = Tomato(input())
tomat_2 = TomatoBush(5, 1000)

# print(tomat_2.print_ii)
print(tomat_2.grow_all())
