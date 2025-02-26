class Car:
    total_car = 0


    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cars are good"
    
    @property
    def model(self):
        return self.__model
    
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"

#my_tesla = ElectricCar("Telsa", "Model S", "85kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# print(my_tesla.__brand)
#print(my_tesla.fuel_type())

safari = Car("tata", "safari")



#safari.model = "city"
# print(safari.fuel_type())
# #print(Car.total_car)
# print(safari.model)

# print(Car.general_description())



# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "sierra")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("tesla", "model z")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())