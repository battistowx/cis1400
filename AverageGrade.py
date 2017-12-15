# Author: Chris Battisto
# Date: 10/15/2014
# Program: AverageGrade.py
# Descr:
# Program that takes an input of five percentage grades, calculates
# the average grade, and displays a letter grade for that average.
def main():
    counter=4
    listScores=[]
    listGrades=[]
    for counter in range(0,5):
        localScore=getValidScore()
        listScores.append(localScore)
    indexCounter=0
    for counter in range (0,5):
        grade=str(determineGrade(listScores, indexCounter))
        listGrades.append(grade)
        indexCounter=indexCounter+1
    print('Your Grades Are: ',listGrades)
    print('Your Average Percentile is: ', calcAverage(listScores))
    
    
def getValidScore():
    scoreInput=float(input('Input a score:'))
    isInvalidScore(scoreInput)
    if isInvalidScore(scoreInput)==True:
        return scoreInput
    else:
        print('Input a score above 0 and below 100')
        main()
        

def isInvalidScore(scoreInput):
    if scoreInput >=0.0 and scoreInput <=100.0:
        valid=True
        return valid
    else:
        valid=False
        return valid

def determineGrade(listScores, indexCounter):
    if listScores[indexCounter] <60.0:
        return 'F'
    elif listScores[indexCounter] >=60.0 and listScores[indexCounter] <=69.9:
        return 'D'
    elif listScores[indexCounter] >=70.0 and listScores[indexCounter] <=79.9:
        return 'C'
    elif listScores[indexCounter] >=80.0 and listScores[indexCounter] <=89.9:
        return 'B'
    elif listScores[indexCounter] >=90.0 and listScores[indexCounter] <=100.0:
        return 'A'

def calcAverage(listScores):
    totalPercentile=float(listScores[0]+listScores[1]+listScores[2]+listScores[3]+listScores[4])
    average=totalPercentile / 5
    return average
    

main()

##OUTPUT:
##Input a score:101
##Input a score above 0 and below 100
##Input a score:-1
##Input a score above 0 and below 100
##Input a score:98.5
##Input a score:45.6
##Input a score:87.4
##Input a score:95.5
##Input a score:65.0
##Your Grades Are:  ['A', 'F', 'B', 'A', 'D']
##Your Average Percentile is:  78.4
##Input a score:
