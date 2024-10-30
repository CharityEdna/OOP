# TASK 5:USING super() FUNCTION
# The super() function is used to give access to methods and properties of a parent or sub class.

class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def __init__(self, brand, power, drumsize):
        super().__init__(brand, power)
        self.drumsize = drumsize

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Power: {self.power}W")
        print(f"Drum Size: {self.drumsize}")

# instance of the object appliance
washing_machine = WashingMachine("Samsung", 1000, "10")
washing_machine.show_details()

  

        