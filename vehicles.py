class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        print ("a Vehicle ahas been created")
    def display_info(self):
        print (f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nnum_doors: {self.num_doors}")


    def display_vin(self):
        print("VIN:1234567890")

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make,model,year,weight)
        self.num_doors = num_doors
        print ("A car has been created")

    def display_info(self):
        print (f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nnum_doors: {self.num_doors}")

    def honk(self):
        print("HONK")

bmw = Car("BMW","M3",2020, 1003, 2, )
print(bmw.display_info())

class Boat(Vehicle):
    def __init__(self, make, model, year, weight, boat_type):
        super().__init__(make,model,year,weight)
        self.boat_type = boat_type

    def display_info(self):
        print(f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nboat_type: {self.boat_type}")

    def honk(self):
        print("HRUNNNKKKKK")

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, num_doors,payload_capacity):
        super().__init__(make,model,year,weight)
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

    def display_info(self):
        print (f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nnum_doors: {self.num_doors}\npayload_capacity: {self.payload_capacity}")

    def honk(self):
        print("HJOOOOOOOOONNNNNNNNNNNKKKKKKKKKK")
    def dump_load(self):
        print("DUMPING LOAD")


if __name__ == "__main__":
    # Create instances of Vehicle Car
    car = Car("Toyota", "Corolla", 2021, 1275.0,4)
    truck= Truck("Mac", "Street 750", 2019, 220.0,4, 350) #<--- but this now takes truck's constructor.

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the motorcycle
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    print()
