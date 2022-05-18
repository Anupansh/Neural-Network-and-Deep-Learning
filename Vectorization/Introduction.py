# Vectorization is a process of lessening the number of for loops in
import math
import time
import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Without vectorization
c = 0
tic = time.time()
for i in range(100000):
    c += a[i] * b[i]
toc = time.time()
print("Time taken to run for loop", (toc - tic) * 1000, "ms with value", c)

# With vectorization
tic = time.time()
c = np.dot(a, b)
toe = time.time()
print("Time taken to run vectorized version", (toe - tic) * 1000, "ms with value ", c)

# Another example


n = 1000000
v = np.random.random(n)
u = np.zeros((n, 1))

# Without Vectorization
tic = time.time()
for i in range(n):
    u[i] = math.exp(v[i])
toc = time.time()
print("Time taken to run for loop", (toc - tic) * 1000, "ms")

# Without Vectorization
tic = time.time()
u = np.exp(v)
toc = time.time()
print("Time taken to run for loop", (toc - tic) * 1000, "ms")