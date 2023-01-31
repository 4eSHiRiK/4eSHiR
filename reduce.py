# Функция Reduce()
# reduce(функция, итерируемый объект, начальное значение)
# Применяет функцию двух аргументов к элементам итерируемого объекта.
# Функции требуется два аргумента, первый из которых является первым элементом в
# итерируемый объект(если начальное значение не указано) а второй - вторым элементом
# в итерируемый объект. Если начальное значение указано, то оно становится первым
# аргументом функции функции, а первый элемент в  итерируемый объект становится вторым элементом.
# Функция reduce "уменьшает"  итерируемый объект до одного значения.

from functools import reduce
items = [2, 3, 4, 5]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, items, 10)
print(result)

items_max = reduce(lambda a, b: a if (a > b) else b, items)
print(items_max)

items_multiplication = reduce(lambda num1, num2: num1 * num2, items)
print(items_multiplication)