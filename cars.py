class Car(object):
    """Car class"""
    def __init__(self, make = "", year = 0, miliage = 0, colour = ""):
        self.make = make
        self.year = year
        self.miliage = miliage
        self.colour = colour

    def drive(self, km):
        self.miliage += km

    def repaint(self, new_colour):
        self.colour = new_colour

car1 = Car()
car1.make = "Volvo"
car1.year = 2005
car1.miliage = 150000
car1.colour = "green"

car2 = Car()
car2.make = "Opel"
car2.year = 2015
car2.miliage = 55000
car2.colour = "red"

car3 = Car('BMW', 1986, 850000, 'black')
