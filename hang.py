from Classes.wordlist import WordList
from Classes.HanganGame import HangmanGame

def get_difficulty():
    """
    Validates if the user input is correct
    """
    option = str(raw_input("Please, select the difficulty: [1] Easy | [2] Hard "))
    while(option != '1' and option != '2'):
        print("That's not a option! Come on user, you can do it!")
        option = str(raw_input("Please, type a valid choice "))

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
    


difficulty = get_difficulty()
wordlist = WordList()
secretWord = wordlist.get_secret_word(difficulty)
hangman(secretWord)