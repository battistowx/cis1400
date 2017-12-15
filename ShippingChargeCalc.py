# Author: Chris Battisto
# Date: 09/24/2014
# Program: ShippingChargeCalc.py
# Descr:
# Program made to take weight of a package
# and multiply it by a given rate to display
# a final package charge amount.

def shippingChargeCalc(weight, rate, chargeAmount):
    chargeAmount=weight*rate
    print('The shipping charge is $',chargeAmount)
    return

def main():
    chargeAmount=float(); rate=float()
    weight=int(input('Input the package weight: '))
    shippingDecide(weight)
    return

def shippingDecide(weight):
    if weight<=2:
        rate=1.10
    if weight>2 and weight<6:
        rate=2.2
    if weight<6 and weight<9:
        rate=3.7
    if weight>=10:
        rate=3.8
    shippingChargeCalc(weight, rate, chargeAmount)
    return
    
main()

## Sample run:
## Input the package weight: 10
## Input the shipping rate: 5
## The shipping charge is $ 50.0
