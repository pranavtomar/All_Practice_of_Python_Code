def create_largest_number(number_list):
    sort_numbers = sorted(number_list,reverse=True)
    string_list = [str(i) for i in sort_numbers]
    res = "".join(string_list)
    return int(res)
    #remove pass and write your logic here
    
    

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)

