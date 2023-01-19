import os
#
# s = '\n'
# print(s.split(), s.splitlines())
#
# s = 'ab c\nde fg\rkl\r\n'
# print(s.split(), s.splitlines())
# ['ab', 'c', 'de', 'fg', 'kl'] #split
# ['ab c', 'de fg', 'kl']       #splitlines



# Если переменная вне функции (меняется только внутри функции)
# val = 5
# def func():
#     val = 15
#     print(val)
#
# func()
# print(val)
#

# f = open('example.txt', 'r')
# print(f)
# print(*f)
#
# f.close()
# with open('example.txt', 'r') as f:
#     print(*f)

# with open('example.txt', 'r') as f:
#     print(f.read(4))
#     print(f.read())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#
# with open('new_file.txt','w') as f:
#     print(f)
#     f.write('Hello my friend')

# os.rename('new_file.txt','my_new_file.txt')
# print(f'Current catalog is {os.getcwd()}')
# print(f"Make directory {os.mkdir('new_dir_les_13')})")
# print(f"Change directory {os.chdir('new_dir_les_13')}")
# print(f"Make directory {os.mkdir('new_dir_les_13_1')})")
# os.makedirs('dir_1/dir_2/dir_3')
# os.remove('new_dir_les_13/example.txt')
# os.rmdir('dir_1/dir_2/dir_3')
# os.removedirs('dir_1/dir_2')

# with open('example.txt', 'r') as f:
#     t = f.readline()
#     sum = 0
#     for elem in t:
#         if elem.isdigit():
#            sum += int(elem)
#     print(sum)

# with open('example.txt') as f:
#     my_str = f.readlines()
#     print(my_str)
#     my_str = my_str[0] # From list into str
#     print(my_str)
#     my_str = my_str.replace('_',' ') #оставили только пробелы как разделители
#     print(my_str)
#     my_str = my_str.split()#Список с числами и словами
#     print(my_str)
#     sum = 0
#     for i in my_str:
#         if i.isdigit():
#             sum += int(i)
#     print(sum)


# with open('example.txt') as f:
#     num_lst = []
#     word_lst = []
#     total_lst = []
#     t = f.readlines()
#     for i in t:
#         if type(i) is int:
#             num_lst += i
#
#         elif type(i) is str:
#             word_lst += i
#     num_lst.sort()
#     word_lst.sort()
#     total_lst = num_lst.append(word_lst)
#     print(total_lst)

# with open('example.txt') as f:
#     num_lst = []
#     word_lst = []
#     my_str = f.readlines()
#     for i in my_str:
#         elem = i.strip()
#         if elem.isdigit():
#             num_lst.append(int(elem))
#         elif elem.isalpha():
#             word_lst.append(elem)
#     num_lst.sort()
#     word_lst.sort()
#     total_lst = num_lst+word_lst
#     print(total_lst)



f_name = input('enter file name')
with open(f_name,'w') as f:
    while True:
        text = input('Enter your text')
        if text == '':
            break
        else:
            f.write(text)




#
# with open('example.txt') as f:
#     line = 0
#     for i in f:
#         line += 1
#         print(f'{len(i)-1}')
#         print(f'{line}:{len(i.strip())}')
#     print(f'Kol-vo strok {line}')


