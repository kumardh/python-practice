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