# Если в функцию передаётся кортеж, то посчитать длину
# всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Cтрока – кол-во букв.
# Cделать проверку со всеми этими случаями.


# def proverka(x):
#     if type(x) is tuple:
#         total = {}   # Через словарь
#         # tot = ''   #Через строку
#         for elem in x:
#             if type(elem) is str:
#                 total.update({elem:len(elem)})
#                 # tot += f'Длина слова {elem} - {len(elem)} букв; '
#         return total
#     elif type(x) is list:
#         number = 0
#         letter = 0
#         for elem_1 in x:
#             if type(elem_1) is int:
#                 number += 1
#             elif type(elem_1) is str:
#                 for l in elem_1:
#                     letter += 1
#         return f'Количество букв равно {letter}, а чисел - {number}'
#     elif type(x) is int:
#         nechet = 0
#         for num in str(x):
#             if int(num) % 2 != 0:
#                 nechet += 1
#         return f'Количество нечетных цифр {nechet}'
#     elif type(x) is str:
#         letters = 0
#         for word in x:
#             if word.isalpha():
#                 letters += 1
#             else:
#                 continue
#         return f'Количество букв равно {letters}'
#     else:
#         return f'Введенный формат данных не найден'
#
#
#
# print(proverka((1,3,'hello','world')))
# print(proverka([1,3,'hello','world']))
# print(proverka(581894543))
# print(proverka('hello23'))
