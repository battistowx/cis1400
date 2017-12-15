# Author: Chris Battisto
# Date: 11/5/2014
# Program: AverageNumbers.py
# Descr:
# This program reads the numbers in the file numbers.dat and
# calculates the average of those numbers.

def main():
    averageList=[]
    average=float()
    numRead=0
    nameFile=open('C:\\Users\\win7\\Desktop\\numbers.dat')#or different path for each computer
    #averageListLine represents each line to be inserted into the list for averaging
    averageListLine=nameFile.readline()
    while averageListLine!='':
        numRead+=1
        averageList.append(int(averageListLine))
        averageListLine=nameFile.readline()
    nameFile.close()
    average=sum(averageList)/numRead
    print('The average is: ',average)

main()

##OUTPUT:
##The average is:  59.285714285714285

    
    
   
    
