# MarsMemory.py Final Group Project
# Authors: Chris Battisto, Kathy Meier, Azbi Zekiri
# Date: 12/15/14
# Descr:
# This game displays numbers and challenges the user to memorize
# as many as they can to get awarded donuts.  If they do not
# memorize the numbers in the right order or input the wrong number,
# then they lose!    

import random

################################
#Tkinter GUI:
################################

# import tkinter module/package/workspace and
# allow direct reference to all contained objects
from tkinter import *

# create class definition of GUI window
class MarsMemory_GUI:
    # constructor/initializer creates and places widgets
    def __init__(self):
        # create window and set titile
        self.mainWindow = Tk()
        self.mainWindow.title('Simon Game')
        self.mainWindow.geometry('500x410')

        # create test labels and text boxes
        # Use Grid Manager to place in rows and columns
        # Test 1 Input -> first row
        self.welcomeLabel = Label(self.mainWindow, \
                                  
                                  text = str('Welcome to the Memory MARS!\n' +
                                   'The Computer will display a number (0 thru 9).\n You must type the number and press\n' +
                                   'SPACE then hit ENTER. With every iteration\n you must type the previous numbers\n' +
                                   '(each followed by SPACE) BEFORE you type the new number.\n' +
                                   'If you type an incorrect number you LOSE!:') )
                                  
                                

        self.welcomeTextBox = Entry(self.mainWindow, width = 10)
        self.welcomeLabel.grid(row = 0, column = 0)

        # Number String -> 1st row
        self.numbersLabel = Label(self.mainWindow, \
                                 text = 'Numbers:')
        self.numbersShowLabel = Label(self.mainWindow, \
                                   text = '')
        self.numbersLabel.grid(row = 1, column = 0)
        self.numbersShowLabel.grid(row =1, column = 1)

        # your guess input -> second row
        self.userLabel = Label(self.mainWindow, \
                                text = 'Enter your Guess:')
        self.userTextBox = Entry(self.mainWindow, width = 10)
        self.userLabel.grid(row = 2, column = 0)
        self.userTextBox.grid(row = 2, column = 1)

        # Create the labels and place in grid 
        self.result2Label = Label(self.mainWindow, \
                                 text = 'Your Score:')
        self.yourScoreLabel = Label(self.mainWindow, \
                                   text = '')
        self.result2Label.grid(row = 3, column = 0)
        self.yourScoreLabel.grid(row =3, column = 1)

        # Create the labels and place in grid 
        self.result3Label = Label(self.mainWindow, \
                                 text = 'Previous High Score:')
        self.highScoreLabel = Label(self.mainWindow, \
                                   text = '')
        self.result3Label.grid(row = 4, column = 0)
        self.highScoreLabel.grid(row =4, column = 1)

        # create buttons and place in grid 
        self.compButton = Button(self.mainWindow, \
                                 text = 'Enter your guess', \
                                 command=self.compButton_Click)
                                 
        self.exitButton = Button(self.mainWindow, \
                                 text = 'Exit', \
                                 command=self.mainWindow.destroy)

        self.playButton=Button(self.mainWindow, \
                               text='Play', \
                               command=self.playButton_Click)
        
        self.playButton.grid(row=5,column=0)                         
        self.calcButton.grid(row = 5, column = 1)
        self.exitButton.grid(row = 6, column = 0)

        #CREATE CLICK FUNCTIONS
    def compButton_Click(self):
        userInput()
        


        # enter the main event loop
        self.mainWindow.mainloop()


################################
#Mars Memory Class:
################################

class Mars_Memory:
    def setGenerateList(self, generateList):
        #generate a 10-item list of random numbers between 0 and 9
        generateList=[]
        for i in range (10):
            generateList.append(random.randrange(0,15,1))
        self.generateList=generateList

    def getGenerateList(self):
        return self.generateList

################################
#Modules:
################################

    
def userInput():
    # Declare variables
    # mList = masterList
    # uList = userList; w is the variable to collect numbers
    mars=Mars_Memory()
    marsGUI=MarsMemory_GUI()
    generateList=mars.setGenerateList(generateList)
    mList=mars.getGenerateList()
    print(mList)
    uList = []
    w = str()
    index = 0
    windex= -1
    score = 0
    correct = True
    while correct == True:
        windex=windex+1
        print('The number is: ',mList[index])
        w = marsGUI.yourGuessLabel.get()
        uList.insert(windex,w)
        timer(mList)
        if comp(mList[:index+1], uList[:])==True:
            index = index + 1
            MarsMemory_GUI.yourScoreLabel = Label(self.mainWindow, \
                                   text = score)
            score = score + 1000
        else:
            self.numbersShowLabel = Label(self.mainWindow, \
                                   text = 'You lose!')
            correct = False
    finalScore(score)


def comp(m, u):
    done = len(u)
    i = 0
    compare = True
    while i < done:
        if m[i] == u[i]:
            i = i + 1
           # print(i)
        else:
            compare = False
            i = i + 1
    return compare

def finalScore(score):
    highScore = ()
    myScore = open('C:\\Users\\Christopher\\Desktop\\HighestScore.txt', 'r+')
    highScore = myScore.readline().rstrip('\n')
    print('The previous highscore is: ',highScore, 'donuts')
    if score > highScore:
        myScore.close()
        myScore = open('C:\\Users\\Christopher\\Desktop\\HighestScore.txt', 'w+')
        highScore = score
        print('Congratulations!  Your score or', score, 'donuts is the new high score!')
        myScore.write(highScore)
    else:
        print('Shucks, your score of', score ,'donuts is not the new highscore.')
    myScore.close()

def timer(mList):
    import time
    blank=[]
    seconds=2
    startTime=time.time()
    finishTime=startTime+seconds
    while time.time()<finishTime:
        self.numbersShowLabel = Label(self.mainWindow, \
                                   text = mList[:index+1])
        
    self.numbersShowLabel = Label(self.mainWindow, \
                                   text = mList[:index+1])
        

##########################
#Main module:
##########################

def main():
    myMarsMemory=MarsMemory_GUI()
    
    
main()

