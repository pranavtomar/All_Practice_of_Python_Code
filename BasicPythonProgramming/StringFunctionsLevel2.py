def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    num_count = 101
    for i in range(no_of_passengers):
        strng = ''
        strng += airline+":"+source[0:3]+":"+destination[0:3]+":"+str(num_count+i)
        ticket_number_list.append(strng)
    if no_of_passengers > 5:
        ticket_number_list = ticket_number_list[-5:]
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",10))