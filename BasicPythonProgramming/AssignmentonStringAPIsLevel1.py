def remove_duplicates(value):
    #start writing your code here
    unique_str = ""
    for char in value:
        if char not in unique_str:
            unique_str += char
    return unique_str

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))