#Создайте классы Car и CarRental. Класс Car должен представлять автомобиль
# с атрибутами make, model и year. Класс CarRental должен управлять арендой
# автомобилей.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


class CarRental:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, make, model):
        self.cars = [car for car in self.cars if not (car.make == make and car.model == model)]

    def find_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                return car
        return None


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
rental = CarRental()
rental.add_car(car1)
rental.add_car(car2)
print(rental.find_car("Honda", "Civic").get_info())