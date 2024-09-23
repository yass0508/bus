class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self):
       
        super().__init__(seating_capacity=50)

    def fare(self):
       
        total_fare = super().fare()
        
        maintenance_charge = total_fare * 0.10
       
        return total_fare + maintenance_charge



if __name__ == "__main__":
    bus = Bus()
    print("Total fare for the bus ride is INR:", bus.fare())
