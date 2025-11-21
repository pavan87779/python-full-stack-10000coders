class Vehicle:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)
class Car(Vehicle):
    def __init__(self,brand,model,price,number_of_doors):
        super().__init__(brand,model,price)
        self.number_of_doors=number_of_doors
    def info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)
        print("Number of Doors: ",self.number_of_doors)

class Bike(Vehicle):
    def __init__(self,brand,model,price,engine_cc):
        super().__init__(brand,model,price)
        self.engine_cc=engine_cc
    def info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)
        print("Engine CC: ",self.engine_cc)

class Truck(Vehicle):
    def __init__(self,brand,model,price,load_capacity):
        super().__init__(brand,model,price)
        self.load_capacity=load_capacity
    def info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)
        print("Load Capacity: ",self.load_capacity)
        
car = Car("BMW",2022,5000000,4)
car.info()
print("---------------------------------------")
bike = Bike("Royal Enfiled",2023,300000,"350CC")
bike.info()
print("---------------------------------------")
truck = Truck("Mahindra",2018,2000000,"4tuns")
truck.info()



"""
Brand:  BMW
Model:  2022
Price:  5000000
Number of Doors:  4
---------------------------------------
Brand:  Royal Enfiled
Model:  2023
Price:  300000
Engine CC:  350CC
---------------------------------------
Brand:  Mahindra
Model:  2018
Price:  2000000
Load Capacity:  4tuns
"""