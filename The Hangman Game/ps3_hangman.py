# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string/
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0;
    for letter in lettersGuessed:
      i=0
      check= []
      while( i < len(secretWord)):
       if secretWord[i] == letter:
         if letter not in check:
           check= letter
           count += 1
       i += 1
    if count == len(secretWord):
       return True
    else:
       return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    check = ''
    for letter in secretWord:
      i=0 
      while( i < len(lettersGuessed)):
       if lettersGuessed[i] == letter:
         check= check + letter
       i += 1
    #print check
    res= []
    i=0
    while(i< len(secretWord)):
        if secretWord[i] not in check:
            res.insert(i,str(' _ '))
        else:
            res.insert(i,secretWord[i])
        i += 1
    #print res
    ans= ''
    for var in res:
        ans= ans+ var
    return ans
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha= string.ascii_lowercase
    res=[]
    for al in alpha:
        res.append(al)
    
    for var in lettersGuessed:
        j=0
        while(j< len(res)):
            if res[j]==var:
                res.remove(var)
            j += 1
    
    ans=''
    for var in res:
        ans= ans+ var
    return ans

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    i=8
    lettersGuessed=[]
    guess=''
    print '------------'
    while(i > 0):
     #print '\n'
     print 'You have '+str(i)+' guesses left.'
     avail= getAvailableLetters(lettersGuessed)
     print 'Available letters: '+ avail
     guess= raw_input("Please guess a letter:")
     guessInLowerCase = guess.lower()
     lettersGuessed.append(guessInLowerCase)
     if (guessInLowerCase in avail and guessInLowerCase in secretWord):
         print 'Good guess: '+ getGuessedWord(secretWord, lettersGuessed)
         print '------------'
         if (secretWord==getGuessedWord(secretWord, lettersGuessed)):
           break
     elif(guessInLowerCase in avail and guessInLowerCase not in secretWord):
         print 'Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed)
         print '------------'
         i -= 1
     elif(guessInLowerCase not in avail):
         print 'Oops! You\'ve already guessed that letter: '+ getGuessedWord(secretWord, lettersGuessed)
         print '------------'
     
    if (secretWord==getGuessedWord(secretWord, lettersGuessed)):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was '+secretWord




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
