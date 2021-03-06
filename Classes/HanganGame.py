import string

class HangmanGame(object):
	
	def __init__(self, secret_word):
		self.__secretWord = secret_word
		self.__guessesLeft = 8
		self.__lettersGuessed = []
		self.__all_letters = string.ascii_lowercase

	def start(self):

		while self.__guessesLeft > 0:

			if (self.isWordGuessed()):

				print 'Congratulations, you won!'
				break

			else:
				
				print 'You have ', self.__guessesLeft, 'guesses left.'
				available = self.getAvailableLetters()
				print 'Available letters', available
				letter = self.get_input()

				if letter in self.__lettersGuessed:
					text = 'Oops! You have already guessed that letter: '

				elif letter in self.__secretWord:
					self.__lettersGuessed.append(letter)
					text = 'Good Guess: '

				else:
					self.__lettersGuessed.append(letter)
					self.__guessesLeft -=1
					text = 'Oops! That letter is not in my word: '

				guessed = self.setGuessedWord()
				self.message(text, guessed)

		else:
			print 'Sorry, you ran out of guesses. The word was ', self.__secretWord, '.'

	def isWordGuessed(self):

	    for letter in self.__secretWord:
	        if letter in self.__lettersGuessed:
	            pass
	        else:
	            return False
	    return True

	def getAvailableLetters(self):
	    letters = self.__all_letters
	    for letter in letters:
	        if letter in self.__lettersGuessed:
	            letters = letters.replace(letter, '')
	    return letters

	def setGuessedWord(self):
		guessedWord = ''
		for letter in self.__secretWord:
			if letter in self.__lettersGuessed:
				guessedWord += letter
			else:
				guessedWord += '_ '
		return guessedWord

	def message(self, text, guessed):
	    print text + guessed
	    print '------------'

	def get_input(self):
		"""
		Validating user entry
		"""
		numbers = ['0','1','2','3','4','5','6','7','8','9']
		user_input = raw_input('Please guess a letter: ')
		while user_input in numbers or user_input == '':
			print('Noooops Bad Choice, :(')
			user_input = raw_input('Try Again, digit something valid: ')
		return user_input
		