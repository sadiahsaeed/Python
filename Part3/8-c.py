from random import choice
from re import match


def get_input( _regex, _string ):
	"""validates input from console
		by matching with _regex
	    args: regular expression, _string to display to user
	    returns: valid input
	"""
	while True:
		line = input( _string )
		if match( _regex, line ): break
		else: pass
	return line


def generate_random_word( ):
	with open('file.txt', 'r') as f:
		line = f.read( ).split('\n')
	return choice(line)


def get_indexes( _word, _char ):
	""" returns the index of all occurrences of _char
	    args: word to iterate, char to look for
	    returns: a list of the indexes of _char
	"""
	return [i for i, letter in enumerate(_word) if letter == _char or letter == _char.upper()]


def guess_letters( word ):
	""" guess the letters of the word
		check if letter is in word if is place in its correct location
		in display
	    args: None
	    returns: None
	"""
	tries, incorrect = [], 0
	display = [ '_' for i in range ( len ( word ) ) ]
	print(display)

	while '_' in display:
		if incorrect == 6:
			print('You lose!')
			return False
		char = get_input('^[a-zA-Z ]$', '\nEnter your guess, one letter or one space: '.format(6 - incorrect))
		if char in set(tries) or char.upper() in set(tries):
			print("You have already guessed {0}!".format(char))
			continue
		elif char in word or char.upper() in word:
			indexes = get_indexes(word, char)
			for index in indexes:
				display[index] = char
		else:
			incorrect += 1
			print("{0} is not in this word!".format(char))
			draw_man(incorrect)
			print("\nYou have {0} guesses left!".format(6 - incorrect)) #TODO: correct plural

		if incorrect < 6:
			tries.append(char)
			print( display )
	return True


def play_game ( ):
	""" wrapper function to play the game until user enters n or N
	    args: None
	    returns: None
	"""
	word = generate_random_word()
	print_banner()
	guess_letters ( word )


	while True:
		line = get_input ( '^[ynYN]$', 'You Win! Would you like to play again? [y|n]' )
		if line == 'y' or line == 'Y':
			word = generate_random_word( )
			print_banner()
			guess_letters ( word )
		else:
			break

# TODO: Clean this up
def draw_man(turn):
	if turn == 1:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
                
		print ( '|==========' )

	if turn == 2:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
		print ( '|       | ' )
		print ( '|         ' )
		print ( '|         ' )
		print ( '|==========' )

	if turn == 3:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
		print ( '|      /|' )
		print ( '|         ' )
		print ( '|         ' )
		print ( '|==========' )

	if turn == 4:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
		print ( '|      /|\ ' )
		print ( '|         ' )
		print ( '|         ' )
		print ( '|==========' )

	if turn == 5:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
		print ( '|      /|\ ')
		print ( '|      /  ' )
		print ( '|         ' )
		print ( '|==========' )

	if turn == 6:
		print ( ' ________' )
		print ( '|       |' )
		print ( '|       |' )
		print ( '|       0' )
		print ( '|      /|\ ' )
		print ( '|      / \ ' )
		print ( '|         ' )
		print ( '|==========' )

def print_banner():
	print ( '\n***********************' )
	print ( 'Welcome to Hang Man!' )
	print ( '***********************' )
	print ( 'Guess one letter at a time' )
	print ( 'Game is not case sensitive\n' )

if __name__ == "__main__":
	play_game( )
