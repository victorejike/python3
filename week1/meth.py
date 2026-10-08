# now lets create a class
class Vehicle:
    has_engine = True

    # The constructor method (used during instantiation)
    def __init__(self, make, model, color):
        # This instance variable (unique to each object)
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"the {self.color} {self.make} engine is now working to run")


# ================================================
# 2 child class


class car(Vehicle):
    # FIXED: Changed _init_ to __init__ (double underscores)
    def __init__(self, make, model, color, number_of_doors):
        # FIXED: Changed _init_ to __init__ (double underscores)
        super().__init__(make, model, color)

        self.number_of_doors = number_of_doors

    def open_trunk(self):
        print(f"opening the trunk of the {self.model}.")


# ==================================
# 3
# ===============================

car1 = car("Toyota", "camry", "Red", 4)
car2 = car("Tesla", "model 3", "Blue", 4)

print("--Accessing Attributes/instanc")
print(f"car 1 is a {car1.color} {car1.make}.")
print(f"car 2 is a {car2.color} {car2.make}.")

print(f"Does Car 1 have an engine? {car1.has_engine}")
print(f"Does car 2 have an engine? {car2.has_engine}")

print(f"\n--- sending Message / Method Calls ---")
car1.start_engine()
car2.open_trunk()
