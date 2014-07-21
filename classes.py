####################################################
### Introduction to Classes                      ###
### Exercises from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python   ###
####################################################

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3
    
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False
            
my_triangle = Triangle(90,30,60)

print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


### Car class exercises ###

class Car(object):
    def __init__(self, model, color, mpg):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a {0} {1} with {2} MPG.".format(self.color, self.model, self.mpg)

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg   = mpg

my_elec_car = ElectricCar("Fiat", "blue", 45, "molten salt")

my_car = Car("DeLorean", "silver", 88)

print my_car.condition
print my_car.display_car()

# __repr__ exercise

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
my_point = Point3D(1, 2, 3)

print my_point