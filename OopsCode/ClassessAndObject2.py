class Item:
    def __init__(self, item_id, price_per_unit, description):
        self.item_id = item_id
        self.price_per_unit = price_per_unit
        self.description = description

class Customer:
    def __init__(self, customer_name, bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount
    def purchase(self):
        self.bill_amount = 0.95*self.bill_amount #bill_amount after discount
        self.pays_bill(self.bill_amount)
    def pays_bill(self, amount):
        print(f"{self.customer_name} pays bill amount Rs. {amount}")

class Employee:
    def __init__(self,emp_name,designation):
        self.emp_name = emp_name
        self.designation = designation


obj1 = Customer("Pranav", 5000)
obj1.purchase()