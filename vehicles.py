#TASK 3: MULTILEVEL INHERITANCE
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    
    def start(self):
        print(f" {self.vehicle_type} is starting...")


class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors
        
        
        
class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity

    def show_info(self):
        print(f"Vehicle Type: {self.vehicle_type}, Number of Doors: {self.number_of_doors}, Battery Capacity: {self.battery_capacity}")


# creating an object ElectricCar
car = ElectricCar('Electric', 4, 100)
car.start() 
car.show_info()
print(car.vehicle_type) 
 


