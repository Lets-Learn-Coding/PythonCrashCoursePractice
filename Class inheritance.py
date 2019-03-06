# inheritance

class car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #not in the init
        self.odometer_reading = 0

    def desc(self):
        print (self.make + ' ' + self.model)

    def odo(self):
        print ('The odometer reading is ' + str(self.odometer_reading))

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_batt(self):
        print ('This car has a ' + str(self.battery_size) + ' sized battery!')

# make a child class
#call the new class and put the parent class in the ()
class Truck(car):
    def __init__(self, make, model, year):
        #takes the init info from class car
        super().__init__(make, model, year)
        self.battery = Battery()



Truck('car', 'carmry', 2901).desc()
Truck('car', 'truck', 2193).odo()
my_truck = Truck('big', 'ass', 2210)
my_truck.battery.describe_batt()