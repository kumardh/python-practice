# How to print
x=10
y=20
print(x+y)

# A simple function
def sum(x,y):
    return x+y
print(sum(5,2))

# Getting type of a value
f = 101;
print(type(f))

# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)

# Don’t use global keyword unless you know what you are doing. In case you need to retun multiple values return tuple as below -
# Correct method
def profile():
  name = "Danny"
  age = 30
  return name, age
profile_name, profile_age = profile()
print(profile_name)
print(profile_age)

# Incorrect method
def profile():
  global name, age
  name = "Danny"
  age = 30
profile()
print(name)
print(age)

# Reading User input
try :
  x = int(input("Enter number 1: "))
except ValueError:
  x = 0
try :
  y = int(input("Enter number 2: "))
except ValueError:
  y = 0
print("sum: " + str(x+y))

# use while loop
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