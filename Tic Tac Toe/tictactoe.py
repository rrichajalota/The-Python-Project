# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:51:00 2016

@author: Rrich
"""
# Tic- Tac- Toe
import random

# print the board on screen
def showBoard(Board):
    '''The function prints the board on screen.
    Board is a list of 10 strings representing the board.
    '''
    
    print '  |   |  '
    print str(Board[7]) + ' | ' + str(Board[8]) + ' | '+ str(Board[9])
    print '  |   |  '
    print '_ _ _ _ _ _ '
    print '  |   |  '
    print str(Board[4]) + ' | ' + str(Board[5]) + ' | '+ str(Board[6])
    print '  |   |  '
    print '_ _ _ _ _ _ '
    print '  |   |  '
    print str(Board[1]) + ' | ' + str(Board[2]) + ' | '+ str(Board[3])
    print '  |   |  '
    print
    
#Board= [' ' , 'x', ' ', ' ', 'O' , ' ' , ' ', ' ', 'x' , 'O']
#showBoard(Board)

def inputPlayerLetter():
    ''' Ask for player's letter.
        Returns a list with the player’s letter as the first item, 
        and the computer's letter as the second.
    '''
    while (True):
     letter = raw_input('Do you want to be X or O? ')
     if letter == 'X' or letter == 'O' or letter == 'x' or letter == 'o':
        letter= letter.upper()
        if letter== 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
     else:
        print 'Invalid input.'
#print inputPlayerLetter()

def decide():
    ''' Randomly choose the player who goes first.'''
    if random.randint(0,1)==0:
        return 'Computer'
    else:
        return 'Player'

def playAgain():
    '''This function returns True if the player wants to
       play again, otherwise it returns False.
    '''
    while (True):
     again= raw_input('Do you want to play again? (yes/no): ')
     again= again.lower()
     if again== 'yes':
        return True
     elif again == 'no':
        return False
     else:
        print 'Invalid Input.'

def makeMove(Board, letter, move):
    '''place the move on the board'''
    Board[move]= letter

def isWinner(Board, letter):
    '''Given a board and a player’s letter, this function returns True 
    if that player has won.
    '''
    if Board[7]== letter and Board[8]== letter and Board[9]== letter:
        return True
    elif Board[4]== letter and Board[5]== letter and Board[6]== letter:
        return True
    elif Board[1]== letter and Board[2]== letter and Board[3]== letter:
        return True
    elif Board[1]== letter and Board[5]== letter and Board[9]== letter:
        return True
    elif Board[1]== letter and Board[4]== letter and Board[7]== letter:
        return True
    elif Board[2]== letter and Board[5]== letter and Board[8]== letter:
        return True
    elif Board[3]== letter and Board[6]== letter and Board[9]== letter:
        return True
    elif Board[7]== letter and Board[5]== letter and Board[3]== letter:
        return True
    else:
        return False

def getBoardCopy(Board):
    '''Make a duplicate of the board list and return it the duplicate.'''
    dupBoard=[]
    for i in Board:
        dupBoard.append(i)
    return dupBoard

def isSpaceFree(Board, move):
    '''Return true if the passed move is free on the passed board.'''
    return Board[move]== ' '

def getPlayerMove(Board,movesList):
    '''Let the player type in their move.'''
    while (True):
       available= availableMoves(Board,movesList)
       print "Available moves " + str(available)
       move= raw_input('What is your next move? (1-9): ')
       if move in '1 2 3 4 5 6 7 8 9'.split() and isSpaceFree(Board, int(move)):
           return int(move)
       else:
           print 'Invalid Input.'

def availableMoves(Board,movesList):
    ''' returns a list of available moves'''
    available=[]
    for move in movesList:
        if isSpaceFree(Board, move)== True:
            available.append(move)
    return available
    
#Board= [' ' , 'x', ' ', ' ', 'O' , ' ' , ' ', ' ', 'x' , 'O']
#movesList= [1,2,3,4,5,6,7,8,9]
#print availableMoves(Board, movesList)
def ChooseRandomMove(Board,movesList):
    '''Computer chooses a move from the available moves randomly'''
    available= availableMoves(Board,movesList)
    if len(available)!= 0:
        return random.choice(available)    # computer's move
    else:
        return None

def getComputerMove(Board, computerLetter):
    ''' Given a board and the computer's letter, determine where 
    to move and return that move.
    '''
    if computerLetter== 'X':
        playerLetter ='O'
    else:
        playerLetter = 'X'
        
    for i in range(1,10):
        dupBoard= getBoardCopy(Board)
        if isSpaceFree(Board,i)== True: 
            makeMove(dupBoard, computerLetter, i)
            if isWinner(dupBoard, computerLetter)== True:
                return int(i) 
    # Check if the player could win on their next move, and block them.
    for i in range(1,10):
        dupBoard= getBoardCopy(Board)
        if isSpaceFree(Board,i)== True:
            makeMove(dupBoard, playerLetter, i)
            if isWinner(dupBoard, playerLetter)==True:
                return int(i)
    
    # Try to take one of the corners, if they are free.
    move= ChooseRandomMove(Board,[1,3,7,9])
    if move != None:
        return int(move)
        
    #Try to take the center, if it is free.
    if isSpaceFree(Board,5):
        return 5
    #Try to take the sides, if they are free.
    return ChooseRandomMove(Board,[2,4,6,8])
    
def isBoardFull(Board):
   ''' Return True if every space on the board has been taken. 
   Otherwise return False.
   '''
   for i in range(1,10):
       if isSpaceFree(Board,i)==True:
           return False
   return True
   
def sampleBoard(Board):
    '''Returns a sample of the board with position numbers'''
    dupBoard=getBoardCopy(Board)
    i= 1
    while(i < 10):
        dupBoard[i]= i
        i += 1
    showBoard(dupBoard)
    
#Start of the game
print('Welcome to Tic Tac Toe!')
while True:
    #Reset the board
    Board= [' ']*10
    movesList= [1, 2, 3, 4, 5, 6, 7, 8, 9]
    playerLetter, computerLetter= inputPlayerLetter()
    turn= decide()
    print 'The '+ str(turn) + ' will go first'
    print 'This is what the board looks like -> ' 
    sampleBoard(Board)
    gameplaying= True
    while gameplaying:
      if turn == 'Player':
        showBoard(Board)
        move= getPlayerMove(Board, movesList)
        makeMove(Board, playerLetter, move)
        if isWinner(Board, playerLetter):
            showBoard(Board)
            print 'Wuhooooo! You have won the game! :D '
            gameplaying= False
        else:
            if isBoardFull(Board):
                showBoard(Board)
                print 'The game is a tie!'
                gameplaying= False
            else:
                turn = 'Computer'
      else:
          #computer's turn
          move= getComputerMove(Board, computerLetter)
          makeMove(Board, computerLetter, move)
          if isWinner(Board, computerLetter):
            showBoard(Board)
            print 'Sorry! You lost the game! :('
            gameplaying= False
          else:
              if isBoardFull(Board):
                showBoard(Board)
                print 'The game is a tie!'
                gameplaying= False
              else:
                turn = 'Player'
    again= playAgain()
    if not again:
        break
    
    
    

