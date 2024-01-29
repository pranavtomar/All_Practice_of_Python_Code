class Customer:
    def __init__(self, name, age, phone_no, address):
        self.__name = name
        self.__age = age
        self.__phone_no = phone_no
        self.__address = address
    def view_details(self):
        print(self.__name,self.__age,self.__phone_no)
        print(self.__address.get_door_no(), self.__address.get_street(), self.__address.get_area(), self.__address.get_pincode())
    def update_details(self,addr):
        self.__address = addr
class Address:
    def __init__(self, door_no, street, area, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__area = area
        self.__pincode = pincode
    def get_door_no(self):
        return self.__door_no
    def get_street(self):
        return self.__street
    def get_area(self):
        return self.__area
    def get_pincode(self):
        return self.__pincode

    def update_address(self):
        pass

addr1 = Address(222,"5th Lane","Auras",209870)
addr2 = Address(567,"6th Lane","Rahimabad",82006)

cus1 = Customer("Pranav",23,9170983678,addr1)
cus2 = Customer("Kunal",25,9565814219,addr2)

cus1.view_details()
cus1.update_details(addr2)
cus1.view_details()
