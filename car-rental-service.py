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
        print(f"Vehicle {self.brand} {self.model} {self.year} {self.rental_price_per_day} {self.seating_capacity}")



class bike(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day):
        super().__init__(brand, model, year, rental_price_per_day)


        