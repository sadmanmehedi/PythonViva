class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("FLY!")

car1=Car("Toyota","2023")
boat1=Boat("Titanice","2017")
plane1=Plane("Emirates","2010")

for x in (car1,boat1,plane1):
    x.move()