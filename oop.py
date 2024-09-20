class Vehicle:
    def __init__(self, max_speed, milage, seating_capacity ):
        self.max_speed = max_speed
        self.milage = milage
        self.seating_capacity = seating_capacity

    def calculatefare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, max_speed, milage, seating_capacity):
        super().__init__(max_speed, milage, seating_capacity)

    def calculatefare(self):
        base_fare = super().calculatefare()
        maintenance_fare = base_fare*0.1
        return base_fare+maintenance_fare

bus_instance= Bus(120,30,45)
print(bus_instance.calculatefare())



