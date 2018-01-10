sentence = input("Please type a short sentence: ") #assigns sentence input to variable string

if sentence.isalnum:
	sentence = sentence
else: 
	print("This sentence is not valid. Please use a-z and 0-9")
#validates the data

sentence_lower = sentence.lower()

	
words_in_sentence = sentence_lower.split(" ") #breaks apart sentence without the ' ' characters 

#this assigns the words into a list called  words_in_sentence
capitalized_words = [] #this creates a blank list for words
for x in range(1, len(words_in_sentence)): #creates a loop for every word
	word = words_in_setence[x]
    cap_word = word[0].upper() + word[1:] #capitalizes every word
    capitalized_words.append(cap_word) #adds word to new list
output = ' '.join(capitalized_words)
print(output)


