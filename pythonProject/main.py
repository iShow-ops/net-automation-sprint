# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from netmiko import ConnectHandler


def get_device_version(devices):
    connection = ConnectHandler(**devices)
    output = connection.send_command("show mac addr")
    connection.disconnect()
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    device = {
        "device_type": "cisco_ios",
        "host": "10.1.11.2",
        "username": "cisco",
        "password": "cisco",
        "secret": "secret"
    }
    version_info = get_device_version(device)
    print(version_info)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
