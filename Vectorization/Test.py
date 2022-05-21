import copy

import numpy as np

a = [[1, 2], [3, 4], [5, 6], [7, 8]]
b = [[5, 6], [7, 8]]
print("A", a)
print("B", b)
print(np.dot(a, b))

a = [[1, 2]]
b = [[3], [2]]

print(np.dot(b, a))
print(np.dot(a, b))

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr = arr.reshape(4, -1)
print(arr)


def checkDeepCopy(W):
    W1 = copy.deepcopy(W)
    W1 += 1
    print("Inside",W1)

W = checkDeepCopy(4)
print("Outside",W)

x = np.random.rand(3, 2)

y = np.sum(x, axis=0, keepdims=True)
print(y.shape)