import csv
import json

# example_file = open('example.csv',encoding='UTF-8')
# example_reader = csv.reader(example_file, delimiter=";")
# example_data = list(example_reader)
# print(example_data)
# for i in example_data:
#     print(i)
#     date = i[0]
# example_file.close()



# example_file = open('example.csv',encoding='UTF-8')
# example_reader = csv.reader(example_file, delimiter=";")
# example_data = list(example_reader)
# for row in example_data:
#     print(row)
#     string = 'Cтрока №' + str(example_reader.line_num) + ' '
#     for value in row:
#         string = string + value + ' '
#         print(string)
# example_file.close()


# example_file = open('example.csv',encoding='UTF-8')
# example_reader = csv.reader(example_file, delimiter=";")
# example_data = list(example_reader)
# row = 1
# for i in example_data:
#     print(f'string # {row} {i}')
#     row+=1
#

# ex_file = open('write.csv','w',encoding='UTF-8',newline='')
# ex_write = csv.writer(ex_file,delimiter=';')
# ex_data = [['05.04.2015 13:34', 'Яблоки', '73'],['05.04.2015 3:41', 'Вишни', '85'],['06.04.2015 12:46', 'Груши', '14']]
# for i in ex_data:
#     ex_write.writerow(i)
# ex_file.close()

#
# my_str = '{"name": "maxim","id": 1, "email": "example@example.com", "is_admin": "False"}'
# print(type(my_str))
# data = json.loads(my_str)
# print(type(data))
# print(data['id'])
#
# my_str_1 = [{"id": "maxim"},{"id": 1}]
# for i in my_str_1:
#     print(i['id'])

#
# with open('data.json') as f:
#     data = json.load(f)
# print(data)
#
# d = {'name': 'maxim', 'id': 1, 'email': 'example@example.com', 'is_admin': 'False'}
# # string_my = json.dumps(d, ensure_ascii=False)
# # print(string_my)
#
# with open('d.json','w') as f:
#     json.dump(d,f,ensure_ascii=False)







# a = 20
# b = 10
# res = a if a>b else b
# print(f'больше {res}')



