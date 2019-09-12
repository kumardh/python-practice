# Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared) # [1, 4, 9, 16, 25]

# Map allows us to implement this in a much simpler and nicer way. Here you go:
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared) # [1, 4, 9, 16, 25]