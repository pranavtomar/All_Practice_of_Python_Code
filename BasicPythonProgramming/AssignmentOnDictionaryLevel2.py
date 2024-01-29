def find_correct(word_dict):
    #start writing your code here
    count_correct = 0
    count_almost_correct = 0
    count_wrong = 0
    for key,value in word_dict.items():
        if key == value:
            count_correct += 1
        elif len(key) == len(value) and sum([key[i] != value[i] for i in range(len(key))]) <= 2:
            count_almost_correct += 1
        else:
            count_wrong += 1

    return [count_correct, count_almost_correct, count_wrong]
    
    
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))