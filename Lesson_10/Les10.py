import random


# age = 39
# d = {}
# d_1 = {'name':'fiodar','age': age, 5:10}
# print(d_1)

# d = dict(short ='dict', long='dictionary')
# d_2 = dict([(1,1),(3,4)])
# print(d)
# print(d_2)


#
# d_3 = dict.fromkeys(['a','b','c'])
# print(d_3)

# d_4 = dict.fromkeys(['a','b'],100)
# print(d_4)



# gen_lst = [i*3 for i in range(1,5)]
# print(gen_lst)

#
# a = 1
# l = []
# for i in range(1,5):
#     a = i*3
#     l.append(a)
# print(l)


#
# gen_d = {a:a*3 for a in range(1,5)}
# print(gen_d)
# gen_d = {a*3 for a in range(1,5)}
# print(gen_d)

# d_1 = {'person_1' : {'name':'fiodar', 5:10}, person_2 : {'age': 5}}
# d_1['name'] = 'Maxim'
# print(d_1['name'])


# print(d_1.get('age'))
# print(d_1.get('age', 'Неверный ключ'))
# print(d_1.get('name'))
# # print(d_1['age'])

# print(d_1.items())
# print(d_1.keys())
# print(d_1.values())
# for key in d_1.keys():
#     print(key)
# for key in d_1:
#     print(key)
# for key, res in d_1.items():
#     print(key,res)
#
# d_1.pop('name')
# print(d_1)
#
# d_1 = {'person_1' : {'name':'fiodar', 5:10}, 'person_2' : {'age': 5}}
# print(d_1['person_2']['age'])
# print(d_1.get('person_2')['age'])
# for person in d_1.values():
#     print(person)
#     person['name'] = "hi"
# print(d_1)

# k_in_d_1 = 'name' in d_1['person_1']
# print(k_in_d_1)
#
# l1 = ['adress','number','city']
# l2 = ['libnehta','68','Minsk']
# my_dict =dict(zip(l1,l2))
# print(my_dict)
#
# # for i in my_dict:
# #     print(i)
#
# list_of_keys = list(my_dict.keys())
# list_of_keys.sort()
# print(list_of_keys)
#
# new_dict = {}
# for keys in list_of_keys:
#     print(keys,':',my_dict[keys])
#     new_dict[keys] = my_dict[keys]
# print(new_dict)


#TASK 1
# res = {'name':'Max',"age":24,'city':'minsk'}
# person_1 = dict.fromkeys(['name','age','city'])
# values = dict.fromkeys(['Max',25, 'Minsk'])
# res = dict(zip(person_1,values))
# print(res['age'])

#TASK 2
# car = {'BMW':{'model_1':'x6','model_2':'x5','model_3' : 'x3'},'Tesla':{'model_1':'new','model_2':'new_1','model_3':'new_2'}}
# car_2 = {'BMW' : ['x6','x5','x3'],'Tesla': ['new','new_1','new_2']}
# print(car['Tesla']['model_2'])
# print(car_2['Tesla'][1])

#TASK 3
# d1 = {'a':100,'b':200,'c':300}
# d2 = {'a' : 300, 'b' : 200,'d' : 400}
# print(d1['b']==d2['b'])



#TASK 4
# pr=1
# number = {'number':[random.randint(1,10)for i in range(5)]}
# print(number.values())
# for num in number.values():
#     for num_1 in num:
#         pr *= num_1
# print(pr)
#
# pr_1 = 1
# for num in number.get('number'):
#     pr_1 *= num
# print

#TASK 6

# str = 'pythonist'
# lst_1 = []
# lst_2 = []
# for letter in str:
#     lst_1 += [letter]
#     lst_2 += [str.count(letter)]
# result = dict(zip(lst_1, lst_2))
# print(result)
#
#
# my_dict = {}
# str = 'pythonist'
# for letter in str:
#     my_dict[letter] = str.count(letter)
# print(my_dict)

# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)



