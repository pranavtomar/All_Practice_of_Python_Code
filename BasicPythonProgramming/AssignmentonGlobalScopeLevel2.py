#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    avg = sum(list_of_marks) / len(list_of_marks)
    count = 0
    for i in list_of_marks:
        if i > avg:
            count += 1
    count_percetage = count/len(list_of_marks)*100
    return count_percetage
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    freq_list = [0] * 26
    for mark in list_of_marks:
        freq_list[mark] += 1
    return freq_list
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())