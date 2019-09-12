# How to print
x=10
y=20
print(x+y) # 30

# By default its always printed in new line.
x=10
y=20
print(x+y) # 30
print(x*y) # 200

# You can't do like this. Below will return TypeError: must be str, not int
# print("Number is : " + 30)

# Change number to str as below.
print("Number is: " + str(30)) # Number is: 30

# In case you need to print in same line then use "end" as below
x=10
y=20
print(x+y, end=":")
print(x*y)
# 30:200

# Read input from User. Note the entered value is of type str. So use int cast if you need to do some mathematical operation.
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