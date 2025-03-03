ITERATIONS = 1e5  # Number of iterations to execute
 
res = [] * ITERATIONS  # Pre-allocated array

# Profiling
for i in range(ITERATIONS):
    mfence() # Ensure all previous instructions are completed
    start = now()
    load/store 1
    .
    .
    .
    load/store n
    mfence()
    end = now()
    res[i] = end - start