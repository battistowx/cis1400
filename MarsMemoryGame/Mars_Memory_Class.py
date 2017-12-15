# MARSMemory.py Class
# This class generates a random numbered list

from random import random

class Mars_Memory:
    def setGenerateList(self, generateList):
        #generate a 10-item list of random numbers between 0 and 9
        generateList=[]
        for i in range (10):
            generateList.append(random.randrange(0,15,1))
        self.setGenerateList=generateList

    def getGenerateList(self):
        return self.generateList

        
