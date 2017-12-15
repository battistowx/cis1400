# Author:  Chris Battisto
# Date:    11/10/2014
# Program: NameSortSearch.py
# Descr:
# This program organizes an array of 10 names by
# alphabetical order using the bubble sort algorithm
# and allows the user to search for the index of that name in that list.

def main():
    names=["Ross Harrison","Hannah Beauregard","Bob White","Ava Fischer","Chris Rich","Xavier Adams","Sasha Ricci","Danielle Porter","Gordon Pike","Matt Hoyle"]
    index=int()
    bubbleSort(names,len(names))
    displaySortedNames(names,len(names))
    
#The bubbleSort module takes the name array and sorts it using the
#bubble search algorithm to organize them based in alphabetical
#ascending order from a-z.
def bubbleSort(array, arraySize):
    maxElement=int()
    index=int()
    for maxElement in range(arraySize-1,0,-1):
        for index in range(0,maxElement):
            if array[index]>array[index+1]:
                temp=array[index]
                array[index]=array[index+1]
                array[index+1]=temp
                
#The displaySortedNames module displays the sorted names.
def displaySortedNames(array, arraySize):
    index=0
    for index in range(0,arraySize):
        print('Here are the names organized in alphabetical order:')
        print(array)
        getName(array)

#The getName module takes an input of the user's input of a name and
#searches for that name in the names array using the binarySearch module.
def getName(names):
    searchName=str()
    size=5
    index=int()
    searchName=input('Enter a name: ')
    index=binarySearch(names, searchName, size)
    if index!=-1:
        print(searchName,"was found at index",names.index(searchName))
    else:
        print(searchName," was not found.")
              
#The binarySearch module uses the binary search algorithm to find if the
#name exists and will return the index, or return -1.
def binarySearch(array, value, arraySize):
    first=0
    last=arraySize-1
    position=-1
    found=False
    middle=int()
    while (found==False) and (first<=last):
        middle=int((first+last)/2)
        if array[middle]==value:
            found=True
            position=middle
        elif array[middle]>value:
            last=middle-1
        else:
            first=middle+1
    return position

main()

##OUTPUT:
##Here are the names organized in alphabetical order:
##['Ava Fischer', 'Bob White', 'Chris Rich', 'Danielle Porter', 'Gordon Pike', 'Hannah Beauregard', 'Matt Hoyle', 'Ross Harrison', 'Sasha Ricci', 'Xavier Adams']
##Enter a name: Bob White
##Bob White was found at index 1
##Here are the names organized in alphabetical order:
##['Ava Fischer', 'Bob White', 'Chris Rich', 'Danielle Porter', 'Gordon Pike', 'Hannah Beauregard', 'Matt Hoyle', 'Ross Harrison', 'Sasha Ricci', 'Xavier Adams']
##Enter a name: Kim Kardashian
##Kim Kardashian  was not found.
