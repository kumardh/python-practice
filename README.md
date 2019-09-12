#  Learning Python in most quick, easy and effective way

I am coming from C#, JavaScript, Node background. And recently got a chance to work on an existing Machine Learning project written in Python and my journey to learn Python started from that day. The challenge was to learn Machine Learning concepts with a new language. Python Tutorial for Beginners 2019 by Mosh really helped me to understand Python and ML in the 6 hours of Full course. Also, found couple of nice links on my jouney to Python and ML and you can navigate as below -

- [https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=900s](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=900s)
- [http://book.pythontips.com/en/latest/](http://book.pythontips.com/en/latest/)
- [https://www.guru99.com/python-tutorials.html](https://www.guru99.com/python-tutorials.html)

So, After spending 2-3 days I was kind of comfortable with Python and ML but, when it came to writing code I was kind of struggling due to lack of hands-on in Python. So, my approach was to learn the language with a fair hands on the basics and key concepts of the language before deep dive into the popular libraries like, numpy, pandas, sklearn, scipy, matplotlib etc..

This post is dedicated to all the newbies of Python and ML. I have created a git repository for the Python code. This repository will guide you through the step-by-step approach to learn this language. So, go though the codes file by file and practice to write, execute and analyze result. File name and it's order is important and recommend you to follow the same. In most of the places I have pasted the output next to the expression along with some key notes/concepts wherever possible.

Code can be downloaded from my **[python-practice](https://github.com/kumardh/python-practice)** git repository. I am still working on this repository and will be updating this time to time. So stay tuned if you are interested.

Below are 2 examples of what I mean above by order (first 2 character of file name) and inline comments -

**01_basics.py**


```
# How to print
x=10
y=20
print(x+y) # 30

# You can't do like this. Below will return TypeError: must be str, not int
# print("Number is : " + 30)

# Change number to str as below.
print("Number is: " + str(30)) # Number is: 30

# By default its always printed in new line.
x=10
y=20
print(x+y) # 30
print(x*y) # 200

# In case you need to print in same line then use "end" as below
x=10
y=20
print(x+y, end=":")
print(x*y)
# 30:200

# Read input from User. Note the entered value is of type str. So ensure to cast it to int if you need to do some mathematical operation.
x = input("Enter number: ")
print(type(x)) # <class 'str'>
print(int(x)+ 100) # 110

# Handle User Input
try :
  x = int(input("Enter number 1: ")) # enter 10
except ValueError:
  x = 0
try :
  y = int(input("Enter number 2: ")) # enter 20
except ValueError:
  y = 0
print("sum: " + str(x+y)) # sum: 30

# A simple function
def sum(x,y):
    return x+y
print(sum(5,2)) # 7

# Getting type of a value
f = 101;
print(type(f)) # <class 'int'>

# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)

# Don’t use global keyword unless you know what you are doing. In case you need to retun multiple values return tuple as below -
# Recommended method
def profile():
  name = "Danny"
  age = 30
  return name, age
profile_name, profile_age = profile()
print(profile_name) # Danny
print(profile_age) # 30

# Not recommended method
def profile():
  global name, age
  name = "Danny"
  age = 30
profile()
print(name) # Danny
print(age) # 30

# use while loop to force user to enter correct number.
def ReadNumber():
  loopCondition = True
  while loopCondition:
    try:
      num = int(input("Enter number : "))
      loopCondition = False
    except ValueError:
      loopCondition = True
  return num
x = ReadNumber()
y = ReadNumber()
print(x+y)
```

**03_dist.py**
```
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
```

> Disclaimer: As we are at learning stage it's perfectly fine to add some note on what code is doing. But, in your actual project don't ever try to add comments for what code is doing instead you should be capturing why you are writing a code block.
