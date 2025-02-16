def prepare():
    dp_mask_time = now() + dp_mask_duration
    total_size = 0
    for lq, stream in flow_map:
        total_size += len(lq)

    b_out = dp(total_size)
    spin_wait_until(dp_mask_time)

    acquire_quic_lock()
    enqueue_mask_time = now() + enqueue_mask_duration
    # enqueue b_out amount of data from all lqs that are active
    enqueue_data_to_quic(flow_map, b_out)
    spin_wait_until(enqueue_mask_time)
    release_quic_lock()


def quic_worker():
    acquire_quic_lock()
    packets = prepare_quic_packets()
    release_quic_lock()
    udp_send(packets)