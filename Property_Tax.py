# Author:  Chris Battisto
# Date:    12/10/2014
# Program: PropertyTax.py
# Descr:
# This program takes an assessment value and calculates it
# to display the property tax amount for that value.

from tkinter import *

class PropTax_GUI:
    def __init__(self):
        self.mainWindow=Tk()
        self.mainWindow.title('Property Tax')
        self.mainWindow.geometry('200x150')

        # Assessment value input -> first row
        self.valueLabel = Label(self.mainWindow, \
                                text = 'Enter the property value: ')
        self.valueTextBox=Entry(self.mainWindow, width=10)
        self.valueLabel.grid(row=0, column=0)
        self.valueTextBox.grid(row=0, column=1)

        # Property tax rate input -> second row
        self.ptRateLabel = Label(self.mainWindow, \
                                text = 'Enter the property tax rate (in decimal form): ')
        self.ptRateTextBox=Entry(self.mainWindow, width=10)
        self.ptRateLabel.grid(row=1, column=0)
        self.ptRateTextBox.grid(row=1, column=1)

        # Create the assessment labels and place -> third row
        self.assessResultLabel=Label(self.mainWindow, \
                                text = 'Assessment Value:')
        self.assessValueLabel=Label(self.mainWindow, \
                                   text='')
        self.assessResultLabel.grid(row = 2, column = 0)
        self.assessValueLabel.grid(row = 2, column = 1)

        # Create the property tax amt labels and place -> fourth row
        self.proptaxAmtResultLabel=Label(self.mainWindow, \
                                text = 'Property Tax Amount:')
        self.proptaxAmtValueLabel=Label(self.mainWindow, \
                                   text='')
        self.proptaxAmtResultLabel.grid(row = 3, column = 0)
        self.proptaxAmtValueLabel.grid(row = 3, column = 1)
        
        # Create buttons and place -> fifth row
        self.calcButton = Button(self.mainWindow, \
                                 text = 'Calculate', \
                                 command = self.calcButton_Click)
        self.exitButton = Button(self.mainWindow, \
                                 text = 'Exit', \
                                 command = self.mainWindow.destroy)
        self.calcButton.grid(row = 4, column = 0)
        self.exitButton.grid(row = 4, column = 1)

        # enter the main event loop
        self.mainWindow.mainloop()

    def calcButton_Click(self):
        ptRate=float(self.ptRateTextBox.get())
        propValue=int(self.valueTextBox.get())
        propertyTax=(propValue/100)*ptRate
        assess=propValue+propertyTax
        self.assessValueLabel.configure(text=format(assess, '.2f'))
        self.proptaxAmtValueLabel.configure(text=format(propertyTax, '.2f'))
        

def main():
    myPropTax=PropTax_GUI()
    
main()
