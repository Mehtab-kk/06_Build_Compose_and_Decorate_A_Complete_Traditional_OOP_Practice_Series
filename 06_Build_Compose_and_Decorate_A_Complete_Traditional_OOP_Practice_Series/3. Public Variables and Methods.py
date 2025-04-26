class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):     
        print(f"{self.brand} car started! Vroom vroom!")

my_car = Car("Toyota")

print("Brand:", my_car.brand)  


my_car.start()