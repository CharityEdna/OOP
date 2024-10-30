# TASK 6: POYLMORPHISM AND OVERRIDING

class Aniaml:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Aniaml):
    def make_sound(self):
        print("Bark!")

class Cat(Aniaml):
    def make_sound(self):
        print("Meow!")

# Polymorphism function
def make_animal_sound(animal):
    animal.make_sound()

# instance of object Dog and Cat
dog = Dog()
cat = Cat()

# calling methods
make_animal_sound(dog) 
make_animal_sound(cat)





