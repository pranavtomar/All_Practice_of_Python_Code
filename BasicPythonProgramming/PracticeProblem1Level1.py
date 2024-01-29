def add_string(str1):
    #start writing your code here
    if len(str1) < 3:
        return str1
    elif str1.endswith("ing"):
        str1 += "ly"
    else:
        str1 += "ing"
    return str1

str1="amazing"
print(add_string(str1))

