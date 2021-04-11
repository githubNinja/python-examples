class Car:
    def __init__(self, mileage):
        self.mileage = mileage
        self.odo_reading = 0

    def updateOdometer(self, odo_reading):
        self.odo_reading += odo_reading

    def getOdometerReading(self):
        return self.odo_reading


car = Car(10000)
car.odo_reading += 10
print(f"odometer Reading::{car.odo_reading}")
print(f"odometer Reading:Now:::{car.updateOdometer(98)}")
print(f"odometer Reading::{car.odo_reading}")
