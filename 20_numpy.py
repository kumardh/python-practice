#pip3 install numpy

import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85, 1.75]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45,78]

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(height)
print(np_height)
print(type(np_height))

# Calculate bmi - body mass index ( normal: <25, overweight: 25-30, obess: > 30
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)
#if you wanted to know which observations in our BMI array are above 25
print(bmi[bmi > 25])