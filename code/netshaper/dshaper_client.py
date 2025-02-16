class DShaper_Client:
    def init(self):
        setup_shared_memory()  # Contains LQs
        self.flow_map = new Map()  # QUIC Streams <-> LQs
        new Thread(check_lqs_for_data)

    def on_receive(stream, data, connection_status):
        if connection_status == CONNECTION_ESTABLISHED or connection_status == CONNECTION_TERMINATED:
            update_flow_map(stream)  # Add or remove client from flow_map
            notify_to_ushaper(stream, connection_status)  # Use control LQ to update UShaper
            return

        if connection_status == CONNECTION_ONLINE:
            place_data_in_lq(stream, data)

    def check_lqs_for_data():
        # Keep checking LQs for any data to be forwarded to the server
        while True:
            notification = check_control_lq()
            if notification is not None:
                update_flow_map(notification.stream, notification.connection_status)
                notify_to_dshaper_server(notification.stream)
                
            for stream, lq_pair in flow_map:
                if len(lq_pair.to_server) > 0:
                    send_data_to_stream(stream, lq_pair.to_server)