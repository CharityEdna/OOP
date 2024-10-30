# Task 2: MULTIPLE INHERITANCE
# In multiple inheritance, a class can inherit properties and methods from more than one class.

class Camera():
    def take_photo(self):
        print(f"Taking a photo")
   
class Phone():
    def make_call(self):
        print(f"Making a call")

class Smartphone(Camera,Phone):
    pass

# creating an instance or object of the smartphone class
smartphone = Smartphone()

smartphone.take_photo()
smartphone.make_call()
