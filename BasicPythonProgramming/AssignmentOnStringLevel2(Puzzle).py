def encrypt_sentence(sentence):
    #start writing your code here
    #sentence = sentence.lower()
    sen_list = sentence.split(" ")

    for odd_word_index in range(0,len(sen_list),2):
        sen_list[odd_word_index] = sen_list[odd_word_index][::-1]

    for even_word_index in range(1,len(sen_list),2):
        word = ''
        for char in sen_list[even_word_index]:
            if char.lower() not in 'aeiou':
                word += char
        for char in sen_list[even_word_index]:
            if char.lower() in 'aeiou':
                word += char
        even_word = word
        sen_list[even_word_index] = word
    return ' '.join(sen_list)



sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)