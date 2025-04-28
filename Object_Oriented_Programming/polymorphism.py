"""
Definition: The ability of objects of different classes to respond to the same method name in different ways.
"""
class Vehicle:
    def __init__(self, carBrand, carName):
        self.car_brand = carBrand
        self.car_name = carName
    
    def move(self):
        print(f"The car {self.car_name} is accelerating")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def __init__(self, boatName, boatModel):
        Vehicle.__init__(self,carBrand=boatModel, carName=boatName)
    def move(self):
        print(f'The boat {self.car_brand} is sailing')

boat1 = Boat('Bughatti', 'Levrion')
boat1.move()