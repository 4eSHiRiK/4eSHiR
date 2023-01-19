import random

# c = [random.randint(0,100) for i in range(10)]
# print(c)
# #ТОТ ЖЕ САМЫЙ ГЕНЕРАТОР РАНДОМНОГО СПИСКА
# # c1 = []
# # for i in range(10):
# #     c1.append(random.randint(0,100))
# # print(c1)
#
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[-4])
#
# c.append('privet')
# c += ['hello']
# c.insert(2,'world')
# print(c)

l = [1,2,3,4,5]
# l[0] = 0#Меняем значение индекса на новое, которое указано
del l[1], l[0]
# l.remove(5)
print(l)

# l.append([100,200])
# print(l)
# # print(l[-1][0])
# l[-1].remove(100)
# del l[-1][0]
# print(l)

# lst = ['hello', 'world']
# elem = [1,3,6,'a','b','abc',123,456]
# del elem[4:]
# print(elem)
# del elem [:2]
# print(elem)
# del elem [1:3]
# print(elem)

# if 6 in elem:
#     print('Yes')
# else:
#     print('no')


# lst = ['hello']
# lst_1 = ['world']
# # res = lst + lst_1
# # print(res)
# lst.extend(lst_1)
# # print(lst)
# lst.extend('123')
# # print(lst)
# # lst.append(7)
# # print(lst)
#
# # my_1 = lst
# # print(my_1)
#
# lst_2 = lst.copy()
# print(lst_2)
# print(lst)
# print('*'*50)
# lst_3 = list(lst)
# print(lst_3)
# import copy
# lst_4 = copy.copy(lst)
# print(lst_4)
#
# lst_5 = copy.deepcopy(lst)
# print(lst_5)
# print(lst)
# lst.append('111')
# print(lst)
# print(lst_5)




# lst = [1,2,3,4,5,6]
# new_lst = lst[:7]
# print(new_lst)



# l1 = [1,2,3,'meow']
# i = 0
# while i < len(l1):
#     print(l1[i])
#     i+=1
#
# for i in l1:
#     print(i)


# lst = [random.randint(0,100)for i in range(20)]
# print(lst)
# while 20 in lst:
#     index = lst.index(20)
#     # lst.insert(index, 200)
#     # lst.remove(20)
#     #ИЛИ ТАК
#     lst[index] = 200
# print(lst)



lst = [random.randint(0,10) for i in range(7)]
# print(lst)
def proverka(lst):
    chet = 0
    nechet = 0
    for num in lst:
        if num % 2 == 0:
            chet += 1
        else:
            nechet += 1
    if chet > nechet:
        result = 1
    else:
        result = 2
    return result
    func_oper()
result = 0
def func_oper():
    if result == 1:
        sum = 0
        for num_1 in lst:
              sum += num_1
        return sum
    else:
        return lst[0] * lst[2] * lst[5]

proverka(lst)
print(func_oper())



# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we', 'ee',3,[1,2]]
# c = []
# for i in a:
#     if i in c:
#         continue
#     if i in b:
#         c.append(i)
# print(c)


# a = [4,6,'py','tell',78]
# b = [44,'hello',56,'exept',3]
#
# a.extend(b)
# print(a)
# a.insert(3,6)
# print(a)
# for i in a:
#     if str(i).isalpha()
#         a.remove(i)
# a.remove('py')
# a.remove('hello')
# a.remove('tell')
# a.remove('exept')
# print(len(a))