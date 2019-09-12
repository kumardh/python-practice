# dict example
a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'
print(a)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
k = dict1.keys()
print(type(k))
v = dict1.values()
print(v)

# Best way to understand what is available with the type is use 'dir'.
print(dir(dict1))

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#  '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
#  '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
#  'setdefault', 'update', 'values']

# Let's use few
dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print(str(dict1)) # {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print(len(dict1)) # 4
for x in iter(dict1):
    print(x, end = ":") # a:b:c:d:
print("\n")
p1 = dict1.popitem()
print(len(dict1)) # 3
print(p1) # ('d', 400)
print(type(p1)) # <class 'tuple'>

dict2 = dict1.copy()
p1 = dict1.popitem()
print(len(dict1)) # 2
print(len(dict2)) # 3

