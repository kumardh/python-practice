a = ['apple', 'beetroot', 'cake']
print(a[0]) # apple
print(type(a)) # <class 'list'>
print(dir(a))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
#  '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a.append("dhananjay")
# a.clear()
s = a.sort(reverse=True)
# sort() doesn't return any value while, sorted() returns an iterable list.
print(type(s)) # <class 'NoneType'>
for x in a:
  print(x, end =":") # dhananjay:cake:beetroot:apple: