# Функция filter() в Python применяет другую функцию к заданному итерируемому объекту (список, строка, словарь и так далее), проверяя, нужно ли сохранить конкретный элемент или нет. Простыми словами, она отфильтровывает то, что не проходит и возвращает все остальное.
#
# Объект фильтра — это итерируемый объект. Он сохраняет те элементы, для которых функция вернула True. Также можно конвертировать его в list, tuple или другие типы последовательностей с помощью фабричных методов.
#
# В этом руководстве разберемся как использовать filter() с разными типами последовательностей. Также рассмотрим примеры, которые внесут ясность в принцип работы.
#
# Функция filter() принимает два параметра. Первый — имя созданной пользователем функции, а второй — итерируемый объект (список, строка, множество, кортеж и так далее).
#
# Она вызывает заданную функцию для каждого элемента объекта как в цикле. Синтаксис следующий:

# список чисел
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#
# # функция, которая проверяет числа
# def filter_odd_num(in_num):
#     if(in_num % 2) == 0:
#         return True
#     else:
#         return False
#
# # Применение filter() для удаления нечетных чисел
# out_filter = filter(filter_odd_num, numbers)
#
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))
#
#
#
#
# list1 = ["Python", "CSharp", "Java", "Go"]
# list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
#
# # функция, которая проверяет строки на вхождение
# def filter_duplicate(string_to_check):
#     if string_to_check in ll:
#         return False
#     else:
#         return True
#
# # Применение filter() для удаления повторяющихся строк
# ll = list2
# out_filter = list(filter(filter_duplicate, list1))
# ll = list1
# out_filter += list(filter(filter_duplicate, list2))
#
# print("Отфильтрованный список:", out_filter)
#
#
# """
#     Программа для удаления стоп-слов
#     из строки используя функцию filter()
# """
#
# # Список стоп-слов
# list_of_stop_words = ["в", "и", "по", "за"]
#
# # Строка со стоп-словами
# string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."
#
# # lambda-функция, фильтрующая стоп-слова
# split_str = string_to_process.split()
# filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
#
# print("Отфильтрованная строка:a", filtered_str)


"""ДЕКОРАТОРЫ"""

# def decorator(func):
#     def wrapper():
#         print('Функция-оболочка')
#         func()
#     return wrapper()
# #
# #
# def basic():
#     print('Основная функция')
#
# wrapped = decorator(basic)
# print('Cтарт программы')
# basic()
# wrapped
# print('Конец программы')
#
# @decorator
# def basic():
#     print('основная функция')
# #
# basic()

# def deco(func):
#
#     def wrap():
#         print('1',func.__name__)
#         func()
#     return wrap
#
# @deco
# def origin():
#     print('Hell')
#
# origin()


# def deconum(func):
#
#     def wrap(a=[]):
#         func()
#         a.append(1)
#         print(f'func origin was pulled {len(a)} times')
#     return wrap
#
# @deconum
# def origin():
#     print('hi')
# origin()
# origin()
# origin()
# origin()

# def count_func(func):
#
#     def wr(*args):
#         wr.count += 1
#         res = func(*args)
#         print(f'{func.__name__} was pulled {wr.count}')
#         return res
#
#     wr.count = 0
#     return wr
#
# @count_func
# def origin():
#     print('hi')
# origin()
# origin()
# origin()
# origin()


#
# def bold(func):
#     def wr():
#         return "**" + func() + "**"
#     return wr
#
# def italic(func):
#     def wr():
#         return "//" + func() + "//"
#     return wr
#
# @bold
# @italic
# def form_text():
#     return "We're python GODS"
#
# print(form_text())



# def dec(func):
#     def wr(n):
#         print('Func name',func.__name__, '()','with param',n)
#         func(n)
#     return wr
#
# @dec
# def print_sqrt(n):
#     print(n**0.5)
#
# print_sqrt(4)
# f = dec(print_sqrt)
# f(4)


# from datetime import datetime
# import time
#
# def elapsed(func):
#     def wrapper(a,b,delay=0):
#         start = datetime.now()
#         func(a,b,delay)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds() * 1000
#         print(f'>> func {func.__name__} time during (ms): {elapsed}')
#
#     return wrapper
#
# @elapsed
# def add_with_delay(a,b,delay=0):
#     print('sum',a,b,delay)
#     time.sleep(delay)
#     return a+b
#
# print('Start programm')
# add_with_delay(10,20)

def error_handler(func):
    def wrapper(*args,**kwargs):
        ret = 0
        try:
            ret = func(*args,**kwargs)
        except:
            print('>>Error in func', func.__name__)
        return ret
    return wrapper


@error_handler
def div(a,b):
    return a/b

print(div(10,2))
div(10,0)