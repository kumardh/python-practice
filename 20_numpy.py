#pip3 install numpy

import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85, 1.75]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45,78]

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(height) # [1.87, 1.87, 1.82, 1.91, 1.9, 1.85, 1.75]
print(np_height) # [1.87 1.87 1.82 1.91 1.9  1.85 1.75]
print(type(np_height)) # <class 'numpy.ndarray'>

# Calculate bmi - body mass index ( normal: <25, overweight: 25-30, obess: > 30
bmi = np_weight / np_height ** 2

# Print the result
print(bmi) # [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152 25.46938776]

# if you wanted to know which observations in our BMI array are above 25
print(bmi[bmi > 25]) # [27.88755755 28.75558507 25.48723993 25.84368152 25.46938776]

# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
# The Python core library provided Lists. A list is the Python equivalent of an array, but is resizeable and can contain elements of different types.
# So If we ignore the felixibility of different types of list then should list can be replaced by numpy?
# Anser is no. And then reason is Numpy data structures perform better in:
# Size - Numpy data structures take up less space
# Performance - they have a need for speed and are faster than lists
# Functionality - SciPy and NumPy have optimized functions such as linear algebra operations built in.

# memory compared to 64 + 8 * len(lst) + + len(lst) * 28 (list) as against of 96 + n * 8 Bytes (numpy)

# Below is quick test on performance comparision -

import time
import numpy as np

size_of_vec = 100000

def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - t1


t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2)
print("Numpy is in this example " + str(t1/t2) + " faster!")
# Result :
# 0.02343606948852539 0.0008456707000732422
# Numpy is in this example 27.712996898787708 faster!