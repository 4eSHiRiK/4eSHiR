import random


# name = 'name'
# surname = 'surname'
# if name == surname:
#     print("Yes")
# else:
#     print('No')
#
# is_name = (name == surname)
# print(is_name)

#
# some_str = 'hello'
# some_str_1 = "world"
# print(some_str, some_str_1)
#
# some_str_2 = "I can't do it"
# str = 'my lang "Python" is'
# print(str)

# str = '''Hello i'm micro and like "sneakers" '''
# str_2 = """Hi i'm good ""Fell"""""
# print(str)
# print(str_2)

# a = 5
# str_4 = str(a)
# print(str_4)

#
# print(5+5)
# print(str(5)+str(5)+' hi!')
# print('hello '*5)

#TASK 1
# name = input('Enter your name')
# print(f'Hello,', name)
# print((name+' ') *3)

# a = 'Max'

# b = "Hi, " +a
# print(b)
# print(len(b))
#
# c = b[0]
# c1 = b[5]
# c2 = b[-2]
# c3 = b[3]
# print(c)
# print(c1)
# print(c2)
# print(c3)


# b = "Hi, Max"
# s = b[0:3]
# s1 = b[-3:-1]
# print(s)
# print(s1)
# s3 = b[:10:3]
# print(s3)
# s4= b[::1]
# print(s4)
# s5 =b[::2]
# print(s5)

#TASK 2
# num = random.randint(100, 999)
# print(num)
# num = str(num)
# num_1 = num[0] #или сразу num_1 = int(num[0])
# num_2 = num[1]
# num_3 = num[2]
# num_1 = int(num_1)
# num_2 = int(num_2)
# num_3 = int(num_3)
# print(num_1+num_2+num_3)


# name_of_string = 'HeLlo WorLD'
# print(name_of_string.capitalize())
# print(name_of_string.title())
# print(name_of_string.upper())
# print(name_of_string.lower())
# print(name_of_string.swapcase())
# print("PRIVET".isupper())
# print('privet'.islower())
# print('Privet Mir'.istitle())
#
# print(name_of_string[::-1])

#TASK 3
# s = 'Hello World'
# s1='123'
# print(len(s)-1)
# print(s[::3])
# print(s[0]+s[-1])
# print(s.upper())
# print(s[::-1])
# print(s.isdigit())
# print(s1.isdigit())
# print('Hello'.isalpha())

# name_of_string = 'HeLlo WorLD'
# print(''.join(['hello', 'world']))
# print(name_of_string.split(' '))
# print(name_of_string.lower().split('l'))

#TASK 4
# s = 'А роза упала на лапу азорА'
# a = s.split(' ') #s.split() - пробел по умолчанию
# b = ''.join(a)
# print(b)
# print(''.join(s.split(' ')))
# if b == b[::-1]:
#     print('Yes')
# else:
#     print('Nah')

# a = 'Maxim'
# print('ks'.join(a.split("x")))
# print(a.replace("x","ks"))
#
# print(a.find('x'))
# print(a.find('p'))
# print(a.endswith('im'))
# print(a.startswith('a'))
# print(a.index('a'))
# print(a.index('r'))
# print('MA'in a)
# print('xim'in a)


# tr = 'Hello World 1'
# print(tr[6:11],tr[0:5])
# fw = tr[:tr.find(' ')]
# sw = tr[tr.find(' ')+1:]
# k = sw + ' ' + fw
# print(k)
# print(k.replace('1', 'one'))

# print('da '.strip())