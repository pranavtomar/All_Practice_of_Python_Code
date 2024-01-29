def bracket_pattern(input_str):
    #Remove pass and write your code here
    if input_str.startswith(")"):
        return False
    elif input_str.endswith("("):
        return False
    count1 = 0
    count2 = 0
    for char in input_str:
        if char == "(":
            count1 += 1
        elif char == ")":
            count2 += 1
    if count1 == count2:
        return True
    else:
        return False

    
input_str="()((())())"
print(bracket_pattern(input_str))