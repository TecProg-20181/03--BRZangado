from Classes.wordlist import WordList
from Classes.HanganGame import HangmanGame

def checkDifferentLetters(word):
        ## set() is a collection of unique elements
        howMany = set(word)
        return len(howMany)

def hangman(secretWord):

    differentLetters = checkDifferentLetters(secretWord)
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print 'The word has ', differentLetters, ' different letters.'
    print '-------------'

    new_game = HangmanGame()
    new_game.start(secretWord)
    

option = input("Please, select the difficulty: [1] Easy | [2] Hard ")
"""
Validates if the user input is correct
"""
while(option != 1 and option != 2):
    option = input("Please, type a valid choice ")

wordlist = WordList()
secretWord = wordlist.get_secret_word(option)
hangman(secretWord)