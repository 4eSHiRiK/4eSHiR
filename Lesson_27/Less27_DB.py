import random
import sqlite3
# #
# #
# #
# connect = sqlite3.connect('name.db') #create DB
# cursor = connect.cursor()   #create cursor() obj
#
# cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES ('atlantic','ocean')''')
# connect.commit()
# color = 'red'
# type_of_water = 'sea'
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES (?,?)''', (color,type_of_water))
# connect.commit()
#
# cursor.execute('SELECT * FROM tab_1')
# val = cursor.fetchall()
# # val = cursor.fetchone()
# print(val)
#
# print('*'*10)
#
# cursor.execute(''' SELECT * FROM tab_1 WHERE col_1='pacific' ''')
# val_1 = cursor.fetchall()
# # val = cursor.fetchone()
# print(val_1)
# print('*'*10)
# cursor.execute(''' SELECT * FROM tab_1 ORDER BY col_1 ''')
# val_2 = cursor.fetchall()
# # val = cursor.fetchone()
# print(val_2)
# print('*'*10)
# cursor.execute(''' SELECT * FROM tab_1 WHERE col_2 LIKE 's%' ''')
# val_3 = cursor.fetchall()
# # val = cursor.fetchone()
# print(val_3)
# print('*'*10)
#
# cursor.execute(''' DELETE FROM tab_1 WHERE id=22 ''')
# connect.commit()
# cursor.execute(''' DELETE FROM tab_1 WHERE col_1='pacific' ''')
# connect.commit()
# cursor.execute(''' SELECT * FROM tab_1''')
# val_4 = cursor.fetchall()
# print(val_4)
#
# cursor.execute('''UPDATE tab_1 SET col_1='red' WHERE id=8 ''')
# connect.commit()
# cursor.execute(''' SELECT * FROM tab_1''')
# val_5 = cursor.fetchall()
# print(val_5)













#TASK 1
# num = int(input('Enter number of world'))
# connect_2 = sqlite3.connect('name_1.db') #create DB
# cursor_2 = connect_2.cursor()   #create cursor() obj
#
# cursor_2.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INTEGER) ''')
#
# cursor_2.execute('''INSERT INTO tab_2 (col_1, col_2, col_3) VALUES ('New','World', ?)''', (num,))
# connect_2.commit()
#
# cursor_2.execute(''' SELECT * FROM tab_2 ''')
# val_2 = cursor_2.fetchall()
# for elem in val_2:
#     print(elem)


#TASK 2
num_1 = random.randint(0,10)
num_2 = random.randint(0,10)
i = 0
sred = 0
connect_3 = sqlite3.connect('name_2.db') #create DB
cursor_3 = connect_3.cursor()   #create cursor() obj

cursor_3.execute('''CREATE TABLE IF NOT EXISTS tab_3(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER) ''')
cursor_3.execute(''' INSERT INTO tab_3 (col_1, col_2) VALUES (?,?)''', (num_1,num_2))
connect_3.commit()
cursor_3.execute('''SELECT * FROM tab_3 ''')
val_3 = cursor_3.fetchall()
for i in val_3:
    for j in i:
        print(j)
        sred += j
print(sred)
# sr = (sred/(len(val_3)*2))\
# connect_3.commit()
# if sred>len(val_3):
#     cursor_3.execute('''DELETE FROM tab_3 WHERE id=4 ''')
#     connect_3.commit()
# cursor_3.execute('''SELECT * FROM tab_3''')
# val_4 = cursor_3.fetchall()
# print(val_4)



