#Usage of class method
class CustomerCare:
    __helpline=111000
    @classmethod
    def get_helpline(cls):
        return cls.__helpline
class Customer:
    def call_support(self):
        print("Calling ",CustomerCare.get_helpline())
Customer().call_support()
