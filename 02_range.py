# print numbers in range
for x in range(10):
    print(x)

# Question 1: What is the type of range(10)
# Question 2: What is dir of range(10)
y = range(10)
print(type(y)) # <class 'range'>
print(dir(y)) # ['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
print(str(y)) # range(0, 10)
# len is a built-in function to get the length of a collection. It works by calling an object's __len__ magic method.
print(len(y)) # 10

# Important point to note here is __iter__. if an object implement this method then it can be iterated by calling __next__ (avoid using magic method) or next.
i = iter(y)
print(i.__next__()) # 0
print(i.__next__()) # 1
print(next(i))      # 2