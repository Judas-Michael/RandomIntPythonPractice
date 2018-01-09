import random #imports function
randNum = random.randint(1,10) #assigns variable between set parameters 
guess = input("Guess a number between 1 and 10: ")
guess = int(guess) #makes guess an integer
if randNum == guess: #if guess is correct
	print("You got it!")
if randNum >= guess: #if guess is too low
	print("Nope :( Your guess is too low")
if randNum <= guess: #if guess is too high
	print("Nope :( Your guess is too high")
	