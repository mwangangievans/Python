# print('Muide first')

class Vehicle:
    name: str = None
    model: str = None
    price: int = None

    def __init__(self, name, model, price) -> None:
        self.model = model
        self.name = name
        self.price = price


class Car:
    vehicle: Vehicle = None

    def set_car(self, name: str, model: str, price: int):
      self.vehicle = Vehicle(name, model, price)
      return self

    def get_car(self) -> Vehicle:
        return self.vehicle
    
    @staticmethod
    def message():
        print('I have a car')

car = Car()
print(car.set_car("Corrolla", "Toyota", 200000).get_car().model)
        

class User:
    def __init__(self, first_name: str,last_name: str ) -> None:
        self.first = first_name
        self.last = last_name

    def get_first(self) -> str:
        return self.first


class Employee(User):
    def __init__(self, first_name: str, last_name: str, number: str) -> None:
        super().__init__(first_name, last_name)
        self.no = number

    def get_details(self)-> str:
        return self.first + " " + self.last + " " + self.no

Empy1 = Employee("Engeneer","Mwangangi","001") 
print(Empy1.get_details())       

    
        



