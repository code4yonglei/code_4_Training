from numba import jit
import numpy as np
import time


x = np.arange(100).reshape(10, 10)


@jit(nopython=True)
def go_fast(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


# Compilation time is included in the execution time
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (with compilation) = {end - start} s.")


# Now this function is compiled, re-time it executing from cache
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (after compilation) = {end - start} s.")
