# Author: Chris Battisto
# Date: 9/29/2014
# Program: LargeandSmall.py
# Descr:
# Program that takes a user's input of a series of any numbers and
# displays the largest and smallest values of the given series.
    
def displayMaxMin(maximum, minimum):
    print('Maximum: ',maximum)
    print('Minimum: ',minimum)
    return

def welcome():
    print('Pick and input a series of numbers to sort out the largest and smallest numbers.  Input "-99" to indicate the end of the series.')
    return

def calcValue(inputNumber):
    while inputNumber != -99:
        compare=int(input('Enter another number: '))
        if compare==-99:
            displayMaxMin(maximum, minimum)
            break
        if compare<inputNumber:
            maximum=inputNumber
            minimum=compare
        if compare>inputNumber:
            minimum=inputNumber
            maximum=compare
    return
    
def main():
    welcome()
    inputNumber=int(input('Enter a number: '))
    calcValue(inputNumber)
    return

main()

##OUTPUT:
##Pick and input a series of numbers to sort out the largest and smallest numbers.  Input "-99" to indicate the end of the series.
##Enter a number: 1
##Enter another number: 2
##Enter another number: 3
##Enter another number: 4
##Enter another number: 5
##Enter another number: -99
##Maximum:  5
##Minimum:  1

    

    
