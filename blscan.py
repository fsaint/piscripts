# bluetooth low energy scan
from bluetooth.ble import DiscoveryService

service = DiscoveryService()
devices = service.discover(100)

print(devices)
for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))
