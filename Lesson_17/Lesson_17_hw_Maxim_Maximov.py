#
#
# class Handler:
#     def __init__(self):
#         self.data = input('Enter your data')
#         self.vowels = 0
#         self.consonants = 0
#         self.lst_vowels = []
#         self.lst_consonants = []
#         self.number = 0
#
#     def handler(self):
#         if self.data.isalpha():
#             for letter in self.data:
#                 if letter in "aeiouy":
#                     self.vowels += 1
#                     self.lst_vowels += letter
#                 else:
#                     self.consonants += 1
#                     self.lst_consonants += letter
#             if self.vowels*self.consonants <= len(self.data):
#                 return self.lst_vowels
#             else:
#                 return self.lst_consonants
#         if self.data.isdigit():
#             for num in self.data:
#                 if int(num) % 2 == 0:
#                     self.number += int(num)
#                 else:
#                     continue
#                 return self.number*len(self.data)
#
# prover = Handler()
# print(prover.handler())




a = {1,2,3,4}
a.remove(5)
print(a)