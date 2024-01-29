def find_common_characters(msg1,msg2):
    msg1 = msg1.replace(" ","")
    msg2 = msg2.replace(" ","")

    common_characters = ""
    for char in msg1: #Remove pass and write your logic here
        if char in msg2 and char not in common_characters:
            common_characters += char
    
    if not common_characters:
        return -1
    
    return common_characters


#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)