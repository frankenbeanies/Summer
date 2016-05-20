import os

def game():
	story = getStory()
	if story == []:
		return
	else:
		play(story)
		game()

def play(story):
	for i in range(0, len(story)-2):
		word = raw_input("Give me a.... " + story[i][:-1] + ": ")
		story[len(story)-1] = story[len(story)-1].replace("["+str(i+1)+"]", "*" + word + "*")

	print "\n" + story[len(story)-1] + "\n"


def getStory():
	print "Please choose a MadLib. Input 'q' to quit."
	#get madlibs path
	libpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libs')
	#get list of madlibs
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