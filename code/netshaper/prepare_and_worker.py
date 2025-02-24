def prepare():
    # Calculate T_prep
    dp_mask_time = now() + dp_mask_duration

    # Read the queue sizes (L)
    total_size = 0
    for lq, stream in flow_map:
        total_size += len(lq)

    # Apply DP on L to get transmission size
    b_out = dp(total_size)  
    spin_wait_until(dp_mask_time)

    # Acquire the shared lock between prepare and quic_worker
    acquire_quic_lock()
    # Calculate T_enq
    enqueue_mask_time = now() + enqueue_mask_duration
    # enqueue b_out amount of data from all LQs that are active
    enqueue_data_to_quic(flow_map, b_out)
    # Wait for the remaining time and then release the lock
    spin_wait_until(enqueue_mask_time)
    release_quic_lock()


def quic_worker():
    # Acquire the shared lock between prepare and quic_worker
    acquire_quic_lock()
    # Prepare the QUIC packets to be sent out and release the lock
    packets = prepare_quic_packets()
    release_quic_lock()
    # Send the packets using the underlying network stack
    udp_send(packets)