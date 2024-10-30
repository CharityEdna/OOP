# Task 1: SINGLE INHERITANCE
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity

# overriding show info to include storage capacity
    def show_info(self):
        super().show_info() 
        print(f"Storage Capacity: {self.storage_capacity} GB")
    
# creating an object
smartphone = Smartphone('Iphone', 'Iphone15', 9)
smartphone.show_info()
smartphone = Smartphone('Smasung', 'Note10+', 246)
smartphone.show_info()



