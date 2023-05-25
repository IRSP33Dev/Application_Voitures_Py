from cars import Car
from trucks import Truck


class MainApp:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("L'application a demarre.")

    def use(self):
        if self.running:
            print("L'application est en cours d'utilisation.")
        else:
            print("L'application n'est pas encore demarree.")

    def quit(self):
        self.running = False
        print("L'application a ete quittee.")

def print_menu():
    print("--- Gestion des vehicules ---")
    print("1. Ajouter une nouvelle voiture")
    print("2. Consulter les details d'une voiture")
    print("3. Consulter le nombre de voitures par marque")
    print("4. Mettre a jour le kilometrage d'une voiture")
    print("5. Rechercher les voitures par annee")
    print("6. Afficher les voitures avec un kilometrage eleve")
    print("7. Ajouter un nouveau camion")
    print("8. Consulter les details d'un camion")
    print("9. Consulter le nombre de camions par marque")
    print("10. Mettre a jour le kilometrage d'un camion")
    print("11. Quitter")
    print("Choix : ")

def add_car(cars):
    serial_number = int(input("Numero de serie du vehicule : "))
    brand = input("Marque du vehicule : ")
    model = input("Modele du vehicule : ")
    year = int(input("Annee du vehicule : "))
    mileage = int(input("Kilometrage du vehicule : "))

    car = Car(serial_number, brand, model, year, mileage)
    cars.append(car)


def display_vehicle(vehicle):
    print("\n--- Details du vehicule ---")
    print("Numero de serie :", vehicle.serial_number)
    print("Marque :", vehicle.brand)
    print("Modele :", vehicle.model)
    print("Annee :", vehicle.year)
    print("Kilometrage :", vehicle.mileage)

def count_vehicles_by_brand(vehicles, brand):
    brand_count = sum(1 for vehicle in vehicles if vehicle.brand == brand)
    print("Nombre de vehicules de la marque", brand, ":", brand_count)

def update_vehicle_mileage(vehicle):
    new_mileage = int(input("Nouveau kilometrage du vehicule : "))
    vehicle.mileage = new_mileage
    print("Kilometrage mis a jour avec succes.")

def find_vehicles_by_year(vehicles, year):
    print("\n--- Vehicules de l'annee", year, "---")
    found = False
    for vehicle in vehicles:
        if vehicle.year == year:
            display_vehicle(vehicle)
            found = True
    if not found:
        print("Aucun vehicule trouve pour l'annee", year)

def print_vehicles_with_high_mileage(vehicles):
    print("\n--- Vehicules avec un kilometrage eleve ---")
    found = False
    for vehicle in vehicles:
        if vehicle.mileage >= 100000:
            display_vehicle(vehicle)
            found = True
    if not found:
        print("Aucun vehicule avec un kilometrage eleve.")

def add_truck(trucks):
    serial_number = int(input("Numero de serie du camion : "))
    brand = input("Marque du camion : ")
    model = input("Modele du camion : ")
    year = int(input("Annee du camion : "))
    mileage = int(input("Kilometrage du camion : "))

    truck = Truck(serial_number, brand, model, year, mileage)
    trucks.append(truck)

def display_truck(truck):
    print("\n--- Details du camion ---")
    print("Numero de serie :", truck.serial_number)
    print("Marque :", truck.brand)
    print("Modele :", truck.model)
    print("Annee :", truck.year)
    print("Kilometrage :", truck.mileage)

def count_trucks_by_brand(trucks, brand):
    brand_count = sum(1 for truck in trucks if truck.brand == brand)
    print("Nombre de camions de la marque", brand, ":", brand_count)

def update_truck_mileage(truck):
    new_mileage = int(input("Nouveau kilometrage du camion : "))
    truck.mileage = new_mileage
    print("Kilometrage mis a jour avec succes.")

def main():
    cars = []
    trucks = []
    choice = 0

    while choice != 11:
        print_menu()
        choice = int(input())

        if choice == 1:
            add_car(cars)
        elif choice == 2:
            serial_number = int(input("Numero de serie du vehicule : "))
            found = False
            for car in cars:
                if car.serial_number == serial_number:
                    display_vehicle(car)
                    found = True
                    break
            if not found:
                print("Vehicule non trouve avec le numero de serie", serial_number)
        elif choice == 3:
            brand = input("Marque du vehicule : ")
            count_vehicles_by_brand(cars, brand)
        elif choice == 4:
            update_vehicle_mileage(cars[0])
        elif choice == 5:
            year = int(input("Annee : "))
            find_vehicles_by_year(cars, year)
        elif choice == 6:
            print_vehicles_with_high_mileage(cars)
        elif choice == 7:
            add_truck(trucks)
        elif choice == 8:
            serial_number = int(input("Numero de serie du camion : "))
            found = False
            for truck in trucks:
                if truck.serial_number == serial_number:
                    display_truck(truck)
                    found = True
                    break
            if not found:
                print("Camion non trouve avec le numero de serie", serial_number)
        elif choice == 9:
            brand = input("Marque du camion : ")
            count_trucks_by_brand(trucks, brand)
        elif choice == 10:
            update_truck_mileage(trucks[0])
        elif choice == 11:
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()

