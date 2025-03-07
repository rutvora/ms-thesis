# SIZE = 4KB or 4MB
res = []  # Store the observed latencies

cudaEvent_t start, end

while(True):  # Until attacker stops it
    cudaEventRecord(start)  # Store current GPU clock
    cudaMemcpy(dest, src, SIZE)  # Copy SIZE amount of data 
    cudaEventRecord(end)  # Store current GPU clock
    cudaEventSynchronize(end)  # Ensure all previous CUDA calls are completed
    res.append(stop - start)
    