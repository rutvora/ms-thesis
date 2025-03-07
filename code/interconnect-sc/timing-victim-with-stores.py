res = []  # Store the observed latencies
timer = old_timer = now()

# Issue 85 stores
# 85 is an arbitrary number larger than N = 81
store 1
.
.
.
store 85

# Issue a timer, which will block until a scheduler slot opens up
# Then fill the slot again with another store instruction
while(True):  # Until attacker stops it
    timer = now()  # Executed out of order as soon as the scheduler slot opens up
    res.append(timer - old_timer)
    old_timer = timer
    store # Fill the scheduler slot again