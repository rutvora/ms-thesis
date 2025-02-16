class UShaper_Server:
    def init(self):
        setup_shared_memory()  # Contains LQs
        self.flow_map = new Map()  # Client <-> LQs
        start_server(on_receive=self.on_receive)
        new Thread(check_lqs_for_data)

    def on_receive(client, data, connection_status):
        if connection_status == CONNECTION_ESTABLISHED or connection_status == CONNECTION_TERMINATED:
            lqs = assign_lq_pair(client)
            update_flow_map(client, lqs)  # Add or remove client from flow_map
            notify_to_dshaper(client, connection_status)  # Use control LQ to update DShaper
            return

        if connection_status == CONNECTION_ONLINE:
            place_data_in_lq(client, data)

    def check_lqs_for_data():
        while True:
            notification = check_control_lq()
            if notification is not None:
                update_flow_map(notification.client, notification.connection_status)
                update_connection(notification.client, notification.connection_statys)
                
            for client, lq_pair in flow_map:
                if len(lq_pair.to_client) > 0:
                    send_data_to_client(client, lq_pair.to_client)