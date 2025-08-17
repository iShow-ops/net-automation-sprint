from network_device import NetworkDevice

def test_device_init():
    device = NetworkDevice('HQ_DS1', '10.1.10.2', 'cisco_ios', 'cisco', 'cisco')
    assert device.hostname == 'HQ_DS1'
    assert device.ip == '10.1.10.2'