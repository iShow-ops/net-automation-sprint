from netmiko import ConnectHandler


class NetworkDevice:
    def __init__(self, hostname, ip, device_type, username, password):
        self.hostname = hostname
        self.ip = ip
        self.device_type = device_type
        self.username = username
        self.password = password

    def get_facts(self):
        device_params = {
            'device_type': self.device_type,
            'host': self.ip,
            'username': self.username,
            'password': self.password,
        }
        try:
            connection = ConnectHandler(**device_params)
            output = connection.send_command('show version')
            connection.disconnect()
            return output

        except Exception as e:
            return f"Connection failed: {e}"
