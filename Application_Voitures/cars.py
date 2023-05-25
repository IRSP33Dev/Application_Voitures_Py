class Car:
    def __init__(self, serial_number, brand, model, year, mileage):
        self.serial_number = serial_number
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_serial_number(self):
        return self.serial_number

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage


car1 = Car(1, "Toyota", "Corolla", 2020, 50000)
car2 = Car(2, "Honda", "Civic", 2018, 80000)
car3 = Car(3, "Ford", "Mustang", 2019, 60000)
car4 = Car(4, "Chevrolet", "Cruze", 2017, 70000)
car5 = Car(5, "Volkswagen", "Golf", 2021, 40000)
