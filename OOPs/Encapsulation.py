# ENCAPSULATION

# It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

# __ - 2 underscore makes attribute private 
#      class ke andar sabko access
#      class ke bahar nhi milta

# PROBLEM: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self. battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())
print(my_tesla.get_brand())