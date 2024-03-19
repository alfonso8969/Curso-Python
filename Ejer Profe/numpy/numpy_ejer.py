import numpy as np
import pandas as pd


b = np.array([1, 2, 3, 4, 5, 5])

print(b)

pd.arrays.TimedeltaArray._from_sequence(pd.TimedeltaIndex(["1h", "2h"]))

a2 = np.array([[1, 2, 3], [4, 5, 6]])

print("a2: ", a2)

# Convert to DataFrame

df = pd.DataFrame(a2)

print("df: ", df)

# Convert to Series

s = df[0]

print("s = df[0]: ", s)

# Accessing values in a series
v = s.values

print("s.values =  ", v)

a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("a3: ", a3)

print("np zeros: ", np.zeros((3,), dtype=int))

print("np ones: ", np.ones((3, 2)))

print("np empty: ", np.empty([3, 2]))

print("np full: ", np.full(3, 2))

print("np eye: ", np.eye(3))

print("np diag: ", np.diag([1, 2, 3]))

print("np identity: ", np.identity(3))


# Sistema de dos ecuaciones y dos incógnitas
# x + 2y = 1
# 3x + 5y = 2
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
print("solve a, b: ", np.linalg.solve(a, b))
