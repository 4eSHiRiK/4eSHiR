# Типы данных:
# изменяемые - list [], dict, set
# неизменяемые - frozenset, int, float, bool, str, tuple, complex

#Методы которые кидают ошибку

# string.find()                            -   итог -1/index
# string.index                             -   итог IndexError/index
#
# dict.get(key,[value])                    - итог None/value
# dict.pop(key,[value])                    - итог Error/ delete value + give it back
# dict.popitem                             - итог KeyError/delete key:value + give it back
# dict.setdefault()                        - итог key:None/value
# dict.update()                            - итог None
# del dict[key]                            - итог KeyError/delete key
#
# set.discard()                            - итог Good  / delete value
# set.remove()                             - итог Error / delete value


#Ошибки

# string.index
# dict.pop()
# dict.popitem()
# del dict[key]
# set.remove()
