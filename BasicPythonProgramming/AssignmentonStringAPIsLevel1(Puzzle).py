def check_anagram(data1,data2):
    #start writing your code here
    if len(data1) != len(data2):
       return False
       
    list_data1 = list(data1.lower())
    list_data2 = list(data2.lower())
    
    if sorted(list_data1) != sorted(list_data2):
        return False
    
    for i in range(len(list_data1)):
        if list_data1[i] == list_data2[i]:
            return False
    else:
        return True

print(check_anagram("About","table"))