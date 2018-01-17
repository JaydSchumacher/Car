class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.max_speed = speed
        self.miles = mileage
        self.fuel = fuel

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Speed: ' + str(self.max_speed) + 'mph'
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + str(self.miles) + ' mpg'
        if self.price > 10000:
            print 'Tax is: .12'
        else:
            print 'Tax is: .15'

car1 = Car(20000, 100, "Full", 25)
print "Car 1"
car1.displayInfo()

car2 = Car(50000, 125, "Half Full", 20)
print "Car 2"
car2.displayInfo()

car3 = Car(75000, 150, "Quarter Full", 45)
print "Car 3"
car3.displayInfo()

car4 = Car(70000, 110, "Empty", 35)
print "Car 4"
car4.displayInfo()

car5 = Car(30000, 80, "Full", 30)
print "Car 5"
car5.displayInfo()

car6 = Car(10000, 65, "Half Full", 48)
print "Car 6"
car6.displayInfo()