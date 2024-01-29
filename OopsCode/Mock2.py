import random

class Address:
    def __init__(self, door_no, city, pin):
        self.__door_no = door_no
        self.__city = city
        self.__pin = pin
    
    def get_door_no(self):
        return self.__door_no
    
    def set_door_no(self, door_no):
        self.__door_no = door_no
    
    def get_city(self):
        return self.__city
    
    def set_city(self, city):
        self.__city = city
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin


class Customer:
    def __init__(self, name, age, source, destination, address):
        self.__name = name
        self.__age = age
        self.__source = source
        self.__destination = destination
        self.__address = address
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
    
    def get_source(self):
        return self.__source
    
    def set_source(self, source):
        self.__source = source
    
    def get_destination(self):
        return self.__destination
    
    def set_destination(self, destination):
        self.__destination = destination
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address


class RegularCustomer(Customer):
    reg_discount = 12


class Payment:
    def __init__(self, payment_mode):
        self.__payment_mode = payment_mode
    
    def get_payment_mode(self):
        return self.__payment_mode
    
    def set_payment_mode(self, payment_mode):
        self.__payment_mode = payment_mode
    
    def discount_on_payment_mode(self):
        if self.__payment_mode.lower() == 'card':
            return 20
        elif self.__payment_mode.lower() == 'upi':
            return 15
        else:
            return 0


class Booking:
    dest_src = {
        ('Delhi', 'Kolkata'): 660,
        ('Banglore', 'Mumbai'): 1450,
        ('Mysore', 'Hydrabad'): 870,
        ('Lucknow', 'Kerala'): 2600,
    }
    seats_availability = list(range(1, 51))
    booked = []
    counter = 0
    
    def __init__(self, customer_type, name, age, source, destination, address, seat_no):
        self.customer_type = customer_type
        self.customer = RegularCustomer(name, age, source, destination, address) if self.customer_type.lower() == 'regular' else Customer(name, age, source, destination, address)
        self.seat_no = seat_no

    def checking_src_dest(self, src, dest):
        route = f"({src}, {dest})"
        if route in Booking.dest_src:
            return Booking.dest_src[route]
        else:
            print("Bus service is not available.")
            return 0

    @staticmethod
    def checking_seat_availability(seat_no):
        if Booking.seats_available[seat_no - 1]:
            return True
        else:
            print("Seat is already booked.")
            return False
        
    def book(self, payment_mode):
        ticket_price = self.checking_src_dest(self.customer.get_source(), self.customer.get_destination())
        if ticket_price == 0:
            return 0
        if not self.checking_seat_availability(self.seat_no):
            return 0
        Booking.seats_availability[self.seat_no - 1] = False
        Booking.booked.append(self.seat_no)
        if self.customer_type == 'regular':
            ticket_price *= 1 - RegularCustomer.reg_discount / 100
        payment = Payment(payment_mode)
        ticket_price *= 1 - payment.discount / 100
        return ticket_price

    # method to generate ticket and display ticket details
    def generate_ticket(self, payment_mode):
        ticket_price = self.book(payment_mode)
        if ticket_price == 0:
            print('Ticket not booked')
            return
        print('Welcome to Rajesh travels\nYour ticket is booked\nDetails of booked ticket:')
        print(f'Ticket No:-{self.customer.name[:3].upper()}{Booking.counter:04d}')
        print(f'Name: {self.customer.name}')
        print(f'Age: {self.customer.age}')
        print(f'seat no: {self.seat_no}')
        print(f'{self.source} to {self.destination}')
        print(f'Original Ticket price - Rs {int(ticket_price)}-')
        print(f'Total Price = Rs{int(ticket_price)}-')

        # writing the ticket details to a file
        with open('tickets.txt', 'a') as f:
            f.write(f'Ticket No:-{self.customer.name[:3].upper()}{Booking.counter:04d}\n')

add = Address(148, 'Mumbai', 12576)
book = Booking('Customer','Johnny', 28, 'Mysore', 'Hydrabad', add, 27)
book.generate_ticket("Card")
