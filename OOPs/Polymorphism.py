# Anek roop dharan kr sake

# The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with ddifferent behaviors.

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

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self. battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(my_tesla.fuel_type())
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

safari = Car("Tata", "Safari")
print(safari.fuel_type())