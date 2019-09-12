# Reduce is a really useful function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list. For example, if you
# wanted to compute the product of a list of integers.

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product) # 24

# reduce way:
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product) # 24