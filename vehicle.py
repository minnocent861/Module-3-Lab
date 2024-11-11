"""
Author: Maika Innocent
Date: 11/02/2024
This app accepts student first names and last names  and GPAs, then tests if they qualify for the Dean's List or the Honor Roll. 
The program will stop processing if 'ZZZ' is entered as the last name.

"""
#Creation of a super  class called vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Creation of a class called Automobile inherit the attribute from vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


# Main Program
def main():
    print("Enter information about your car:")
    vehicle_type = "car"  # Since we're only considering cars
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    # Create an Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Display the information
    print("Car Information:")
    car.display_info()


if __name__ == "__main__":
    main()

