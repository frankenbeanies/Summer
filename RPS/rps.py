import random

def game():
	choice = raw_input("(r)ock, (p)aper, (s)cissors, or (q)uit: ").lower().strip()
	if choice == 'r':
		play(0)
	elif choice == 'p':
		play(1)
	elif choice == 's':
		play(2)
	elif choice == 'q':
		return

	game()

def play(player):
	ai = random.randint(0,2)
	options = ["rock", "paper", "scissors"]
	print "Computer plays " + options[ai]

	if player == 0:
		if ai == 2:
			print "You win!"
		elif ai == 1:
			print "CPU wins!"
		elif ai == 0:
			print "Tie!"
	elif player == 1:
		if ai == 0:
			print "You win!"
		elif ai == 2:
			print "CPU wins!"
		elif ai == 1:
			print "Tie!"
	elif player == 2:
		if ai == 1:
			print "You win!"
		elif ai == 0:
			print "CPU wins!"
		elif ai == 2:
			print "Tie!"


if __name__ == "__main__":
	game()