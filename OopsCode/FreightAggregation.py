class Freight:
    counter = 198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__freight_id = 0
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_charge = 0
    def validate_weight(self):
        if self.__weight % 5 == 0:
            return True
        else:
            return False
    def validate_distance(self):
        if self.__distance >= 500 and self.__distance <= 5000:
            return True
        else:
            return False
    def forward_cargo(self):
        if self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id():
            self.__freight_id = 200
            self.__freight_charge = self.__weight * self.__distance
        else:
            self.__freight_charge = 0
        print(f"Freight charge = {self.__freight_charge}")

    def get_freight_charge(self):
        return self.__freight_charge
    def get_freight_id(self):
        return self.__freight_id
    def get_recipient_customer(self):
        return self.__recipient_customer
    def get_from_customer(self):
        return self.__from_customer
    def get_weight(self):
        return self.__weight
    def get_distance(self):
        return self.__distance

class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address
    def validate_customer_id(self):
        if len(self.__customer_id) == 6 and self.__customer_id.startswith("1"):
            return True
        else:
            return False

    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_address(self):
        return self.__address
        
from_customer = Customer("101001","Pranav","Tikara_Samad")
recipient_customer = Customer("101002","Sunny","Jharkhand")

freight = Freight(recipient_customer, from_customer,150,60)

freight.forward_cargo()


