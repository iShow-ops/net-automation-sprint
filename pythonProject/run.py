from network_device import NetworkDevice

device = NetworkDevice(
    hostname = 'HQ_DS1',
    ip = '10.1.12.1',
    device_type = 'cisco_ios',
    username = 'cisco',
    password = 'cisco'
)

facts = device.get_facts()
print(facts)

