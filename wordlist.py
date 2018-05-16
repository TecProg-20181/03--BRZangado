import random
import string

class WordList(object):
	
	def __init__(self):
		self.__file_a = "palavras.txt"
		self.__file_b = "words.txt"

	def createWordList(self, file_choice):
	    """
	    Depending on the size of the word list, this function may
	    take a while to finish.
	    """
	    print "Loading word list from file..."
	    # inFile: file
	    inFile = open(file_choice, 'r', 0)
	    # line: string
	    line = inFile.readline()
	    # wordlist: list of strings
	    wordlist = string.split(line)
	    print "  ", len(wordlist), "words loaded."

	    return wordlist

	def get_secret_word(self, option):

		if option == 1:
			file_choice = self.__file_a
		else:
			file_choice = self.__file_b

		wordlist = self.createWordList(file_choice)
		randomWord = random.choice(wordlist).lower()
		testedWord = self.checkNumberOfLetters(randomWord)

		return testedWord

	def checkNumberOfLetters(self, word):
	    while True:
	        if len(word) <= 8:
	            return word