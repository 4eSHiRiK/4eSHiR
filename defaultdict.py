# from collections import defaultdict
#
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# print(sorted(d.items()))

from collections import defaultdict as DD


# Function for returning a default values for the
# keys which are not present in the dictionary
def default_value():
    return "This key is not present"


# Now, we will define the dict
dict_1 = DD(default_value)
dict_1["ABC"] = 1
dict_1["DEF"] = 2
dict_1["GHI"] = 3
dict_1["JKL"] = 4
print("Dictionary: ")
print(dict_1)
print("key pair 1: ", dict_1["ABC"])
print("key pair 3: ", dict_1["GHI"])
print("key pair 5: ", dict_1["MNO"])




# from collections import defaultdict as DD
# dict_1 = DD(lambda: "This key is not present")
# dict_1["ABC"] = 1
# dict_1["DEF"] = 2
# dict_1["GHI"] = 3
# dict_1["JKL"] = 4
# print("Dictionary: ")
# print(dict_1)
# print("key value 1: ", dict_1.__missing__('ABC'))
# print("key value 4: ", dict_1["JKL"])
# print("key value 5: ", dict_1.__missing__('MNO'))
