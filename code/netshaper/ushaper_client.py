class UShaper_Client:
    def init(self):
        setup_shared_memory()  # Contains LQs
        self.flow_map = new Map()  # server_connection <-> LQs
        new Thread(check_lqs_for_data)

    def on_receive(connection, data, connection_status):
        if connection_status == CONNECTION_ESTABLISHED or connection_status == CONNECTION_TERMINATED:
            update_flow_map(connection)  # Add or remove client from flow_map
            notify_to_dshaper(connection, connection_status)  # Use control LQ to update DShaper
            return

        if connection_status == CONNECTION_ONLINE:
            place_data_in_lq(connection, data)

    def check_lqs_for_data():
        # Keep checking LQs for any data to be forwarded to the server
        while True:
            notification = check_control_lq()
            if notification is not None:
                update_flow_map(notification.client, notification.connection_status)
                update_server_conn(notification.client, notification.connection_status)
                    
            for server_conn, lq_pair in flow_map:
                if len(lq_pair.to_server) > 0:
                    send_data_to_server(server_conn, lq_pair.to_server)