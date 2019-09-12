# As the name suggests, filter creates a list of elements for which a function returns true.
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# But careful when dealing with objects. Filter doesn't create a new copy of the object. Instead object reference is
# is passed. So, If you mutate a object in filtered list, original list is also impacted.
def printList(a):
    for x in range(len(a)):
        print(a[x].name)

class Student:
    def __init__(super, name):
        super.name = name

originalList = [Student("abc"),Student("abd"),Student("pqr"),Student("xyz")]
filteredList = list(filter(lambda s: s.name == "abc", originalList))

filteredList[0].name = "dhananjay"
printList(originalList)