import os, random

def game():
	words = getWords()
	if words == []:
		return
	else:
		playGame(random.choice(words).upper().strip(), 6, [])
		game()

def playGame(word, lives, used):
	#give status
	print "You have " + str(lives) + " lives left."
	print "You have made the following guesses " + str(used)
	prog = ""
	comp = ""
	for letter in word:
		if letter == " ":
			prog += "  "
			comp += " "
		elif letter in used:
			prog += letter + " "
			comp += letter
		else:
			prog += "_ "
			comp += "_"
	print prog
	#check win
	if comp == word:
		print "You Win!"
		return
	#get guess
	guess = raw_input("Please guess a letter: ").upper()
	if len(guess) != 1:
		if guess != word:
			playGame(word, lives, used)
		else:
			print "You Win!"
			return
	else:
		used.append(guess)
		if not (guess in word):
			lives -= 1
			if lives == 0:
				print "You Lose! \nThe word was " + word
				return

	playGame(word, lives, used)


def getWords():
	print "Please choose a word list. Input 'q' to quit."
	#get lists path
	libpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lists')
	#get list of lists
	files = os.listdir(libpath)
	#print menu
	i = 1
	for file in files:
		print "\t" + str(i) + " - " + file
		i += 1
	#get selection
	choice = raw_input("")
	if choice == 'q':
		return []
	else:
		with open(os.path.join(libpath, files[int(choice)-1])) as f:
			return f.readlines()

if __name__ == "__main__":
	game()