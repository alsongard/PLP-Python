class Vehicle:
    def __init__(self, name, brand):
        self.carName = name
        self.carBrand = brand
    def details(self, type):
        print(f'The {type} details are: {self.carName} and {self.carBrand}')
    def move(self):
        print(f'The {self.carName} is moving')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def __init__(self, boatName, boatBrand):
        self.boat_name = boatName
        self.boat_brand = boatBrand
        Vehicle.__init__(self, name=boatName, brand=boatBrand)
    
    def move(self, type):
        print(f'the {type} {self.boat_name} is sailing')

class Plane(Vehicle):
        def __init__(self, planeName, planeBrand):
            self.plane_name = planeName
            self.plane_brand = planeBrand
            Vehicle.__init__(self, name=planeName, brand=planeBrand)
    
        def move(self, type):
            print(f'the {type} {self.plane_name} is flying')

user_car_1 =Car('CX', 'Koeinesagn')
user_car_1.details('Car')
user_car_1.move()

print('\n')
user_plane_1 = Plane('Emirates', 'Cargo')
user_plane_1.details('Plane')

user_plane_1.move('plane')

print('\n')
user_boat_1 = Boat('Venon', "Lamborghini")
user_boat_1.move('boat')
user_boat_1.details('boat')