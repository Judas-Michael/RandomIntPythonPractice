sentence = input("Please type a short sentence: ") #assigns sentence input to variable string
words_in_sentence = sentence.split(" ") #breaks apart sentence without the ' ' characters 

#this assigns the words into a list called  words_in_sentence
capitalized_words = [] #this creates a blank list for words
for word in words_in_sentence: #creates a loop for every word
    cap_word = word[0].upper() + word[1:] #skips the first word0 and capitalizes every word after
    capitalized_words.append(cap_word) #adds word to new list
output = ' '.join(capitalized_words)
print(output)


