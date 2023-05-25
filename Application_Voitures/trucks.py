class Truck:
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


truck1 = Truck(1, "Ford", "F-150", 2020, 50000)
truck2 = Truck(2, "Chevrolet", "Silverado", 2018, 80000)
truck3 = Truck(3, "Dodge", "Ram", 2019, 60000)
truck4 = Truck(4, "Toyota", "Tacoma", 2017, 70000)
truck5 = Truck(5, "GMC", "Sierra", 2021, 40000)
