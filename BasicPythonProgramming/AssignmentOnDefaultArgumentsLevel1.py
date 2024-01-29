def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func is None:
        filtered_data = list_of_num
    else:
        filtered_data = filter_func(list_of_num)
    return sum(filtered_data)

def even(data):
    even_list = []
    for num in data: #Remove pass and write the logic here
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def odd(data):
    odd_list = []
    for num in data: #Remove pass and write the logic here
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list


sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))







