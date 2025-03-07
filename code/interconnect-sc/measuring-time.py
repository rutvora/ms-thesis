res = []  # Store the observed latencies

# Explore from N = 1 to N = 256
# 256 is an arbitrary value larger than (3*size_sched + size_stq)
for i in range(256): 
    timer = now()
    # Do i stores
    store 1
    .
    .
    store i
    res.append(now() - timer)