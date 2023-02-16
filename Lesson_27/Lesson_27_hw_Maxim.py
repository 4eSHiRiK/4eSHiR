import sqlite3
import random

#TASK 3

# num_1 = random.randint(0,10)
# num_2 = random.randint(0,10)
# i = 0
#
# connect = sqlite3.connect('butterfly.db')
# cursor = connect.cursor()
#
#
# cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
# cursor.execute(''' INSERT INTO tab_1 (col_1, col_2) VALUES (?, ?) ''', (num_1,num_2))
# connect.commit()
#
# cursor.execute(''' SELECT * FROM tab_1''')
# length = cursor.fetchall()
# print(length)
# r = random.randint(1, len(length))
# print(r)
# cursor.execute(''' SELECT col_1,col_2 FROM tab_1 WHERE id=?''', (r,))
# all_1 = cursor.fetchall()
# print(all_1)
# for elem in all_1:
#     for elem_1 in elem:
#         if elem_1 % 2 == 0:
#             i += 1
# print(i)
# if i == 2:
#     cursor.execute(''' DELETE FROM tab_1 WHERE id=?''', (r,))
# elif i == 0 or 1:
#     cursor.execute(''' UPDATE tab_1 SET col_1=2,col_2=2 WHERE id=?''', (r,))
# connect.commit()
# cursor.execute(''' SELECT * FROM tab_1''')
# res = cursor.fetchall()
# print(res)



#TASK 4

# connect = sqlite3.connect('task2.db')
# cursor = connect.cursor()
#
# cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
# connect.commit()
#
#
#
#
#
# class Num:
#
#     def count(self,num_1 = None, num_2 = None, num_3 = None):
#         if num_1 is not None and num_2 is None and num_3 is None:
#             cursor.execute(''' INSERT INTO tab_2 (col_1) VALUES (3) ''')
#             connect.commit()
#         elif num_1 is not None and num_2 is not None and num_3 is None:
#             if type(num_2) is int:
#                 cursor.execute(''' DELETE FROM tab_2 WHERE id=1 ''')
#                 connect.commit()
#         elif num_1 is not None and num_2 is not None and type(num_3) is int:
#             cursor.execute(''' UPDATE tab_2 SET col_1=77 WHERE id=3 ''')
#             connect.commit()
#
# num_all = Num()
# num_all.count(1,1,1)
# cursor.execute(''' SELECT * FROM tab_2''')
# res = cursor.fetchall()
# print(res)



#TASK 5
#
# connect = sqlite3.connect('task5.db')
# cursor = connect.cursor()
#
#
# cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_3 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# # cursor.execute(''' INSERT INTO tab_3 (col_1, col_2) VALUES ('Uchiha', 'Shisui') ''')
# # connect.commit()
# # cursor.execute(''' DELETE FROM tab_3 WHERE id=2 ''')
# # connect.commit()
# # cursor.execute(''' UPDATE tab_3 SET col_1='Hello',col_2='World' WHERE id=3 ''')
# # connect.commit()
#
# cursor.execute(''' SELECT * FROM tab_3''')
# check = cursor.fetchall()
# print(check)
#
# with open('database.txt','a') as f:
#     for data in check:
#         f.write('\n')
#         for elem in data:
#             f.write(f'{elem}   ')

# Как сделать чтобы столбики начинались с 1 уровня?

#TASK 6

lst = ['Uchiha',13,5,'Shisui',94,'Sacra']

connect = sqlite3.connect('task_HW.db')
cursor = connect.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_num (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_text (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
connect.commit()

cursor.execute(''' SELECT * FROM tab_num''')
check = cursor.fetchall()
if len(check) > 5:
    cursor.execute(''' DELETE FROM tab_text WHERE id=1 ''')
    connect.commit()
elif len(check) < 5:
    cursor.execute(''' UPDATE tab_text SET col_1 = 'Hello' WHERE id=1''')

for elem in lst:
    if type(elem) is str:
        cursor.execute(''' INSERT INTO tab_text (col_1) VALUES (?) ''', (elem,))
        cursor.execute(''' INSERT INTO tab_num (col_1) VALUES (?) ''', (len(elem),))
        connect.commit()
    elif type(elem) is int:
        if elem % 2 == 0:
            cursor.execute(''' INSERT INTO tab_num (col_1) VALUES (?) ''', (elem,))
            connect.commit()
        else:
            cursor.execute(''' INSERT INTO tab_text (col_1) VALUES ('Нечетное') ''')
            connect.commit()

cursor.execute(''' SELECT * FROM tab_num''')
number = cursor.fetchall()
print(number)
cursor.execute(''' SELECT * FROM tab_text''')
words = cursor.fetchall()
print(words)
