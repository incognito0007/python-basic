# inheritance -- where one class can inherit properties from other class

# class Parent:
#      def __init__(self):
#          self.super_attribute = True
#          print("this is the parent class")
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("this is a child class")
#         print(self.super_attribute)
#
# child1 = Child()


# single inheritance -- one parent class
# multiple inheritance -- two parent class
# multilevel inheritance -- more than two level
#         A class -- grand parent class
#         B class -- parent class
#         C class -- child class
# Hierarchical inheritance -- one parent class is inherited to multiple base class
# Hybrid inheritance -- mix of multilevel and hierarchical inheritance


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
        total_fare = vehicle_fare + maintenance_fare
        return total_fare

vehicle1 = Vehicle(50)
print(vehicle1.get_fare())

bus1 = Bus(50)
print(bus1.get_fare())













