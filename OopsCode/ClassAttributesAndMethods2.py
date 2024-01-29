class Ticket:
    counter = 0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = 0
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if (self.__source.lower() == "delhi") and (self.__destination.lower() == "mumbai" or self.__destination.lower() == "chennai" or self.__destination.lower() == "kolkata" or self.__destination.lower() == "pune"):
            return True
        else:
            return False
    
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            self.__ticket_id = self.__source[0]+self.__destination[0] + (f"{0}{Ticket.counter}" if (Ticket.counter) < 10 else f"{Ticket.counter}")
        else:
            self.__ticket_id = None
    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination
    
ticket = Ticket("Pranav","Delhi","Kolkata")
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()
print(ticket.get_ticket_id())
ticket.generate_ticket()

print(ticket.get_ticket_id())
print(ticket.get_passenger_name())
print(ticket.get_destination())
print(ticket.get_source())

