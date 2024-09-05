# Static Method

# A static method is also a method that is bound to the class and not the object of the class.

# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self. battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_tesla.fuel_type())
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

my_car = Car("Tata", "Safari")


print(my_car.general_description())