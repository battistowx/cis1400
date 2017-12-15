# Author: Chris Battisto
# Date: 10/29/2014
# Program: RainfallStatistics.py
# Descr:
# This program takes 12 user inputs for total rainfall in each
# 12 months of the year.  The program then calculates and displays
# the total annual rainfall, the average monthly rainfall, and
# the months with highest and lowest amounts of rain.

def main():
    SIZE=12
    rainfallInput=0.0
    monthNames=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthlyRainfall=[]
    largestRainfall=''
    smallestRainfall=''
    smallestRainfallIndex=int()
    largestRainfallIndex=int()
    totalRain=''
    averageRain=''
    for SIZE in range(0, SIZE):
       print('Enter the total rainfall in inches for',monthNames[SIZE])
       rainfallInput=float(input())
       monthlyRainfall.append(rainfallInput)
    largestRainfallIndex=GetLargestRainfall(monthlyRainfall)
    largestRainfall=print('Greatest month of rain was', monthNames[largestRainfallIndex], 'with', monthlyRainfall[largestRainfallIndex],'in.')
    smallestRainfallIndex=GetSmallestRainfall(monthlyRainfall)
    largestRainfall=print('Lowest month of rain was', monthNames[smallestRainfallIndex], 'with', monthlyRainfall[smallestRainfallIndex],'in.')
    total=getTotalRain(monthlyRainfall)
    totalRain=print('Total Rainfall: ',total,'in.')
    averageRain=print('Average Rainfall: ',getAverageRain(total),'in.')
    
    
    
    
# Function Name: GetLargestRainfall
# Parameter: Floating List monthlyRainfall
# Returns: The index number of the largest number in list monthlyRainfall
# Descr:
# This function takes an input of the monthlyRainfall and calculates which index has the
# largest number.  The function then returns the index of that number to display the
# greatest total rainfall.
def GetLargestRainfall(monthlyRainfall):
    maxTotal=monthlyRainfall.index(max(monthlyRainfall))
    return maxTotal


# Function Name: GetSmallestRainfall
# Parameter: Floating List monthlyRainfall
# Returns: The index number of the smallest number in list monthlyRainfall
# Descr:
# This function takes an input of the monthlyRainfall and calculates which index has the
# smallest number.  The function then returns the index of that number to display the
# lowest total rainfall.
def GetSmallestRainfall(monthlyRainfall):
    minTotal=monthlyRainfall.index(min(monthlyRainfall))
    return minTotal

# Function Name: getTotalRain
# Parameter: Floating List monthlyRainfall
# Returns: The sum of rain 
# Descr:
# This function takes an input of the monthlyRainfall list and adds all of its
# items.  The function then returns that number to the main module.
def getTotalRain(monthlyRainfall):
    sumRain=sum(monthlyRainfall)
    return sumRain

# Function Name: getAverageRain
# Parameter: Integer total
# Returns: The average amount of rain 
# Descr:
# This function takes an input of the total integer and calculates the
# average by dividing this number by 12.  This then returns the value
# back to the main module.
def getAverageRain(total):
    average=total / 12
    return average
    
main()


##OUTPUT:
##Enter the total rainfall in inches for January
##3.3
##Enter the total rainfall in inches for February
##2.3
##Enter the total rainfall in inches for March
##5.3
##Enter the total rainfall in inches for April
##6
##Enter the total rainfall in inches for May
##3.5
##Enter the total rainfall in inches for June
##2.3
##Enter the total rainfall in inches for July
##5.63
##Enter the total rainfall in inches for August
##6.335
##Enter the total rainfall in inches for September
##9.2
##Enter the total rainfall in inches for October
##1.2
##Enter the total rainfall in inches for November
##3.2
##Enter the total rainfall in inches for December
##0.9
##Greatest month of rain was September with 9.2 in.
##Lowest month of rain was December with 0.9 in.
##Total Rainfall:  49.165 in.
##Average Rainfall:  4.097083333333333 in.
    
        
