def encode(message):
    count = 1
    newStr = ''
    # for i in range(65,91):
    #     if chr(i) in message:
    #         count = message.count(chr(i))
    #         newStr += str(count)+chr(i)
    # return newStr

    for i in range(1,len(message)):
        if message[i] == message[i-1]:
            count += 1
        else:
            newStr += str(count) + message[i-1]
            count = 1
    newStr += str(count) + message[-1]
    return newStr




    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)