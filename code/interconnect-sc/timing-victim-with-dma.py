ATTACKER_ITERS = 1e4  # Arbitrarily large number
ATTACKER_SIZE = 4KB  # or 4MB

VICTIM_ITERS = 1e3  # One order of magnitude less than ATTACKER_ITERS
VICTIM_SIZE = 4KB  # or 4MB

def attacker():
    res = []  # Store the observed latencies
    
    cudaEvent_t start, end
    
    for i in range(ATTACKER_ITERS):
        cudaEventRecord(start)  # Store current GPU clock
        cudaMemcpy(dest, src, ATTACKER_SIZE)  # Copy SIZE amount of data 
        cudaEventRecord(end)  # Store current GPU clock
        cudaEventSynchronize(end)  # Ensure all previous CUDA calls are completed
        res.append(stop - start)

def victim():
    for i in range(VICTIM_ITERS):  # Until attacker stops it
        cudaMemcpy(dest, src, VICTIM_SIZE)  # Copy SIZE amount of data 
        