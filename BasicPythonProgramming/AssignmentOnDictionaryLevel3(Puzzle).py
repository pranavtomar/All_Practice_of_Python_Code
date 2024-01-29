def max_frequency_word_counter(data):
    word=""
    frequency=0
    #start writing your code here
    #Populate the variables: word and frequency
    word_split = data.split()
    max_frequency = -1
    for i in range(len(word_split)):
        frequency=1
        current_word = word_split[i]
        for j in range(i+1,len(word_split)):
            if word_split[i].lower() == word_split[j].lower():
                frequency += 1
                current_word = word_split[i]
        if frequency > max_frequency:
            max_frequency = frequency
            word = current_word
    print(word,max_frequency)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)