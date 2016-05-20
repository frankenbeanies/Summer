def game():
	phrase = raw_input("Please enter a phrase: ")
	output = "*SQUACK* " + phrase + " *SQUACK*"
	print output
	if phrase == "quit":
		return
	else:
		game()

if __name__ == "__main__":
	game()
