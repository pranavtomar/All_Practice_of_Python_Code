def sms_encoding(data):
    #start writing your code here
    split_word = data.split()
    new_str = []
    for word in split_word:
        if len(word) == 1:
            new_str.append(word)
        else:
            new_word = ''
            for letter in word:
                if letter.lower() not in 'aeiou':
                    new_word += letter
            new_str.append(new_word)
    return ' '.join(new_str)
    
    
    

data="MSD says I love cricket and tennis too"
print(sms_encoding(data))