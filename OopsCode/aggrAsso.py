class Address:
    def __init__(self,door_no,street,city):
        self.door_no=door_no
        self.street=street
        self.city=city

    def print_address(self):
        print("Door No :",self.door_no)
        print("Street : ",self.street)
        print("City : ",self.city)

class Customer:
    def __init__(self,cid,cname,caddress,caddress2):
        self.cid=str(cid)
        self.cname=cname
        self.caddress=caddress
        self.caddress2=caddress2
        
    def print_customer_address(self):
        print("Customer Id : "+ self.cid)
        print("Customer Name : "+self.cname)
        print("Customer Address : "+self.caddress.street)
        print("Customer Address : "+self.caddress2.street)

class Parcel_Delivery:
    def __init__(self,pid):
        self.pid=pid

    def customer_delivery(self,Address):
        print("Door No : ",Address.door_no)

addr1=Address(555,"JN Street","Mumbai")
addr2=Address(556,"JN Street","Lucknow")
cust1=Customer(101,"customer1",addr1,addr2)
cust1.print_customer_address()
pd=Parcel_Delivery("P101")
pd.customer_delivery(addr1)
