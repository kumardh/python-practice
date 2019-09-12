a = ("dhananjay", "manav", "manoj")

print(a) # ('dhananjay', 'manav', 'manoj')
print(type(a)) # <class 'tuple'>
print(a[0]) # dhananjay
# Tuple is immutable. You ll get following error when you try to update value -
# TypeError: 'tuple' object does not support item assignment
a[0] ="kumar"