#Check if "Hello" is one of the types described in the type tuple
print(isinstance("Hello", (float, int, str, list, dict, tuple))) # True

dic = {"a":1, "b":2}
print(type(dic)) # <class 'dict'>
print(isinstance(dic,(int,str))) # False
print(isinstance(dic,dict)) # True
print(isinstance(dic,(int,str,dict))) # True

lst = ["a","b"]
print(type(lst)) # <class 'list'>
print(isinstance(lst,(list))) # True
print(isinstance(lst,(list, int))) # True
print(isinstance(lst,(list, str))) # True
print(isinstance(lst,str)) # False

class myObj:
  name = "John"

y = myObj()
print(type(lst)) # <class 'list'>
print(isinstance(y, myObj)) # True