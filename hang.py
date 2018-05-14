import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadWord():
    
    wordlist = createWordList()
    randomWord = random.choice(wordlist).lower()
    testedWord = checkNumberOfLetters(randomWord)
    return testedWord

def createWordList():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."

    return wordlist

def checkNumberOfLetters(word):
    while True:
        if len(word) <= 8:
            return word
def checkDifferentLetters(word):
    ## set() is a collection of unique elements
    howMany = set(word)
    return len(howMany)

def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def initLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    letters = string.ascii_lowercase


    return letters

def getAvailableLetters(lettersGuessed):
    letters = initLetters()
    for letter in letters:
        if letter in lettersGuessed:
            letters = letters.replace(letter, '')
    return letters

def setGuessedWord(guessedWords,secretWord,lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWords += letter
        else:
            guessedWords += '_ '
    return guessedWords

def message(text, guessed):
    print text + guessed
    print '------------'

def startGame(secretWord, guessesLeft):

    lettersGuessed = []

    while guessesLeft > 0:

        if (isWordGuessed(secretWord, lettersGuessed)):
            print 'Congratulations, you won!'
            break
        else:
            print 'You have ', guessesLeft, 'guesses left.'

            available = getAvailableLetters(lettersGuessed)

            print 'Available letters', available

            letter = raw_input('Please guess a letter: ')

            if letter in lettersGuessed:

                text = 'Oops! You have already guessed that letter: '

            elif letter in secretWord:

                lettersGuessed.append(letter)
                text = 'Good Guess: '

            else:

                lettersGuessed.append(letter)
                guessesLeft -=1
                text = 'Oops! That letter is not in my word: '

            guessed = setGuessedWord(getGuessedWord(),secretWord,lettersGuessed)
            message(text, guessed)

    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

def hangman(secretWord):

    guesses = 8
    differentLetters = checkDifferentLetters(secretWord)
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print 'The word has ', differentLetters, ' different letters.'
    print '-------------'

    startGame(secretWord,guesses)


secretWord = loadWord()
hangman(secretWord)