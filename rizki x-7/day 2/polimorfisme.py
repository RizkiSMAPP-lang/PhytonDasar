class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.brand = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

carl = Car("ford", "Mustang")        #Create a Car class
boat1 = Boat("Iblisa" "Touring 20")  #Create a Boat class
plane1 = Plane("Boeing", "747")      #Create a Plane class

for x in (car1, boat1, plane1):
    x.move()