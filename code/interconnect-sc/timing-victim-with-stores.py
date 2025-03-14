ATTACKER_ITERS = 1e5  # Arbitrarily large number
VICTIM_ITERS = 1e4  # Order of magnitude less than ATTACKER_ITERS
VICTIM_SIZE = 4KB  # or 4MB

def attacker():
    res = []  # Store the observed latencies
    timer = old_timer = now()
    # Issue 85 (> 81) stores
    store 1
    ...
    store 85
    # Issue a timer, which will block until a scheduler slot opens
    # Then fill the slot again with another store instruction
    for i in range(ATTACKER_ITERS):  # Until attacker stops it
        timer = now()  # Executed out of order when slot available
        res.append(now() - old_timer)
        old_timer = timer
        store # Fill the scheduler slot again

def victim():
    for i in range(VICTIM_ITERS):
        cudaMemcpy(VICTIM_SIZE)  # DMA transfer