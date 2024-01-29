class FruitInfo:
    __fruit_name_list = ["Apple","Guava","Orange","Grape","Sweet Lime"]
    __fruit_price_list = [200,80,70,110,60]

    @staticmethod
    def get_fruit_price(fruit_name):
        for list in FruitInfo.get_fruit_name_list():
            if list ==  fruit_name:
               index = FruitInfo.get_fruit_name_list().index(list)
               return FruitInfo.get_fruit_price_list()[index]
        else:
            return -1
        
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type

class Purchase:
    __counter = 101
    def __init__(self, customer, fruit_name, quantity):
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__purchase_id = 0
    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
    
    def calculate_price(self):
        if FruitInfo.get_fruit_price(self.__fruit_name) >= 0:
            price = self.get_quantity()*FruitInfo.get_fruit_price(self.__fruit_name)
            if price == max(FruitInfo.get_fruit_price_list()):
                price = 0.98*price
            if price == min(FruitInfo.get_fruit_price_list()):
                price = 0.95*price
            if self.__customer.get_cust_type() == "wholesale":
                price = 0.90*price
            self.__purchase_id = f"P{Purchase.__counter}"
            Purchase.__counter = Purchase.__counter + 1
            return price
        else:
            return -1

customer = Customer("Pranav","wholesale")
purchase = Purchase(customer,"Orange",5)
print(purchase.calculate_price())
print(purchase.get_purchase_id())
customer = Customer("Pranav","wholesale")
purchase = Purchase(customer,"Apple",2)
print(purchase.calculate_price())
print(purchase.get_purchase_id())
