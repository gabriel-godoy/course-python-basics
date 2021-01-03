#!python3

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    # !r calls wrapper method of self.name, so it puts the quotes to self.name
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print('Disconnected.')


# Class inherits from Device
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capaciy = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)

printer.disconnect()
