
#
# mast = ['bubna', 'pika', 'crest', 'chervi']
# nominal = [i for i in range(1,14)]
# card = []
# for elem_1 in mast:
#     for elem_2 in nominal:
#         card.append(str(elem_2)+ ' ' + str(elem_1))
#
# carddeck = iter(card)
# for i in carddeck:
#     print(next(carddeck))
#     # print(carddeck)

#
# class CardIterator:
#     current = 0
#     def __init__(self, some_objects):
#         self.some_objects = some_objects
#
#
#     def __next__(self):
#         while self.current<len(self.some_objects):
#             result = self.some_objects[self.current]
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
#
# class CardDeck:
#
#     mast = ['bubna', 'pika', 'crest', 'chervi']
#     nominal = [i for i in range(1, 14)]
#     card = []
#     def __iter__(self):
#
#         for elem_1 in self.mast:
#             for elem_2 in self.nominal:
#                 self.card.append(str(elem_2) + ' ' + str(elem_1))
#         # print(self.card)
#         return CardIterator(self.card)
#
#
# carddeck = CardDeck()
# cd = iter(carddeck)
# while True:
#     print(next(cd))





class CardDeck:

    mast = ['bubna', 'pika', 'crest', 'chervi']
    nominal = [i for i in range(1, 14)]
    card = []

    def lst(self):
        for elem_1 in self.mast:
            for elem_2 in self.nominal:
                self.card.append(str(elem_2) + ' ' + str(elem_1))
    def iter(self):
        self.card = self.card
        return self.card
    def next(self):
        x = 0
        choosen_card = self.card[x]
        x+=1
        return choosen_card

carddeck = CardDeck()
z = iter(carddeck)
# for i in one_card:
#     print(i)
print(next(z))