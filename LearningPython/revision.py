# Question -> Create a Bus child class that inherits from the vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.  if the
# Vehicle is Bus instance, we need to add an extra 10% on full fare as a
# maintenance charge. So total fare for bus instance will become the
# final amount = total fare + 10% of the total fare


class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicle_fare = super().get_fare()
        maintenance_fare = 0.1 * vehicle_fare
        total_fare = maintenance_fare + vehicle_fare
        return total_fare

truck = Vehicle(100)

print(truck.get_fare())

bus1 = Bus(100)
print(bus1.get_fare())

