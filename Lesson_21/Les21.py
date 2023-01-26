



#
# evens = [2,4,6,8,10]
# evenIterator = iter(evens)
# print(evenIterator)
# print(list(evenIterator))

# print(next(evenIterator))
# print(next(evenIterator))
# print(next(evenIterator))



class IterationExample:

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        y = self.x
        self.x +=1
        return y

classinstance = IterationExample()
example = iter(classinstance)

print(next(example))
print(next(example))
print(next(example))
print(example.__next__())
for i in example:
    print(i)

# l_c = [i for i in ['helloword']]
# print(l_c)
# l_c_i = iter(l_c)
# print((x for x in ['helloworld']))
# print(l_c_i)
#
# [i for i in ['helloword']]  #Генератор списков
# (x for x in ['helloworld']) #Генератор


# class IterationExample:
#
#     def __iter__(self):
#         self.x = 0
#         return self
#
#     def __next__(self):
#         while self.x <6:
#             y = self.x
#             self.x +=1
#             return y
#         else:
#             raise StopIteration
#
# classinstance = IterationExample()
# example = iter(classinstance)

# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# for i in example:
#     print(i)



# element = [2,4,6,8,10]
#
# def all(num):
#     for n in num:
#         return n

# element = [2,4,6,8,10]
#
# def all(num):
#     for n in num:
#         yield n

# ss = (n for n in element)
# print(ss)

# sall = all(element)
# print(sall)
# print(list(sall))
# print(all(element))
# print(all(element))
# print(all(element))

#
# element = [2,4,6,8,10]
#
# def all(num):
#     for n in num:
#         yield n
#
# some_obj = all(element)
# print(some_obj)
# print(next(some_obj))
# print(next(some_obj))

#
# element = [2,4,6,8,10]
# def func(num):
#
#     return (i for i in num if i%2 == 0)
#
# gen_func = func(element)
# print(gen_func)
# print(next(gen_func))
# print(next(gen_func))

a = (i for i in num if i%2 == 0)

