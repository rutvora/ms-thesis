TOTAL_SCHED_SIZE = 4 * 24
STORE_UNIT_SIZE = 64

res = []  # Store the observed latencies
timer = old_timer = now()

# Issue N stores, where N = TOTAL_SCHED_SIZE + STORE_UNIT_SIZE
store 1
.
.
.
store N

# Issue a timer, which will block until a scheduler slot opens up
# Then fill the slot again with another store instruction
while(True):  # Until attacker stops it
    timer = now()  # Executed out of order as soon as scheduler slot opens up
    res.append(timer - old_timer)
    old_timer = timer
    store  # Fills the scheduler slot again