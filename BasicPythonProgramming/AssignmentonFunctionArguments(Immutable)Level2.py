def check_double(number):
    double_number = number * 2
    
    double = str(double_number)
    num = str(number)

    list_number = []
    list_number_double = []

    for i in num:
        list_number.append(i)
    for i in double:
        list_number_double.append(i)

    list_number.sort()
    list_number_double.sort()

    if list_number == list_number_double:
        return True
    else:
        return False
    


#Provide different values for number and test your program
print(check_double(125874))