class vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Vehicle {self.brand} {self.model} {self.year} {self.rental_price_per_day}")

    def rental_cost(self, days):
        return self.rental_price_per_day * days 
    

    def get_rental_price_per_days(self):
        return self.rental_price_per_days    
    
    def set_rental_price_per_days(self, new_price):
        self.get_rental_price_per_days = new_price
    


class car(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"vehicle: {self.brand} model: {self.model} year: {self.year} rental price: {self.rental_price_per_day} seating capacity: {self.seating_capacity}")



class bike(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        print(f"vehicle: {self.brand} model: {self.model} year: {self.year} rental price: {self.rental_price_per_day} engine capacity: {self.engine_capacity}")


def show_vehicle_info(vehicle):
    vehicle.display_info()


Car = car("Toyota", "Corollo", 2020, 50, 5)
Car.display_info()

Bike = bike("Yamaha", "R1", 2019, 30, 998)
Bike.display_info()

print(f"\nRental cost for Toyota, Corolla for 3 days: ${Car.rental_cost(3)}")
print(f"\nRental cost for Yamaha, R1 for 5 days: ${Bike.rental_cost(5)}")

Car.set_rental_price_per_days(55)
print(f"Modified rental price for Toyota Corolla: ${Car.set_rental_price_per_days(55)}")