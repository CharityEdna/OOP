# Task 7: Multiple Inheritance with super()

class Device:
    def info(self):
        print("Device Information")
class Computer(Device):
    def info(self):
        super().info()
        print("Computer Information")
class Laptop(Computer):
    def info(self):
        super().info()
        print("Laptop Information")

#instance of Laptop
laptop = Laptop()

laptop.info()
