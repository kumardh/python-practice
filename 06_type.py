#Check if "Hello" is one of the types described in the type tuple
print(isinstance("Hello", (float, int, str, list, dict, tuple)))

dic = {"a":1, "b":2}
print(type(dic))
print(isinstance(dic,(int,str)))
print(isinstance(dic,dict))
print(isinstance(dic,(int,str,dict)))

lst = ["a","b"]
print(type(lst))
print(isinstance(lst,(list)))
print(isinstance(lst,(list, int)))
print(isinstance(lst,(list, str)))
print(isinstance(lst,str))

class myObj:
  name = "John"

y = myObj()
print(type(lst))
print(isinstance(y, myObj))