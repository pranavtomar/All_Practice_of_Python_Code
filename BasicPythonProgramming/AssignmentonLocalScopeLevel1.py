def calculate(distance,no_of_passengers):
    revenue = no_of_passengers * 80
    cost_of_fuel = (distance/10) * 70
    profit = revenue - cost_of_fuel
    if profit >= 0:
        return profit
    else:
        return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))