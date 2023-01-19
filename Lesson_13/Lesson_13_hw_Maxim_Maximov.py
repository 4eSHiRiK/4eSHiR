

# massiv = [51,2,'hello', 89,'world',11,'privet','qq','you','nice']
#
# file_name = input('Enter name of new file')
# with open(file_name,'w') as f:
#     num_lst = []
#     word_lst = []
#     new_word_lst = []
#     for elem in massiv:
#         if type(elem) is int:
#             num_lst.append(int(elem))
#         elif elem.isalpha():
#             word_lst.append(elem)
#             if word_lst.index(elem) == 0:
#                 new_word_lst.append(elem)
#             for word in word_lst:
#                 if word_lst.count(elem) == new_word_lst.count(elem):
#                     continue
#                 if elem != word:
#                     if len(elem)<len(word):
#                         new_word_lst.insert(new_word_lst.index(word), elem)
#                     else:
#                         continue
#                 if new_word_lst.count(elem) == 0:
#                     new_word_lst.append(elem)
#     num_lst.sort()
#     total = new_word_lst + num_lst
#     f.write(str(total))


# with open('wood.txt', 'w') as f:
#     ar = ["tool", 34, "model", 900]
#     oz = []
#     ol = []
#     ols = []
#     for i in ar:
#         if type(i) == str:
#             ols.append(i)
#         else:
#             oz.append(i)
#     for i in sorted(ols, f=lambda a: len(a)):
#         ol.append(i)
#     for i in ol:
#         f.write(f'{i}\n')
#     for i in sorted(oz):
#         f.write(f'{i}\n')
