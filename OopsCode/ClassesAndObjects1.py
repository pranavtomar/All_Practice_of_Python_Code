class Vehicle:
    def __init__(self, vehical_id, vehical_type, vehical_cost):
        self.vehical_id = vehical_id
        self.vehical_type = vehical_type
        self.vehical_cost = vehical_cost
    def calculate_premium(self):
        self.premium_amout = 0
        if self.vehical_type == "Two Wheelers":
            self.premium_amout = (2/100)*self.vehical_cost
        elif self.vehical_type == "Four Wheelers":
            self.premium_amout = (6/100)*self.vehical_cost
        else:
            print("Vehical type is not matching")
    def display(self):
        #self.calculate_premium()
        print("Vehical Id: ", self.vehical_id)
        print("Vehical cost: ", self.vehical_cost)
        print("Vehical premium_cost: ", self.premium_amout)

obj1 = Vehicle(102,"Two Wheelers",20000)
obj1.calculate_premium()
obj1.display()

