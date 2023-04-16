'''
Created on Sep 15, 2022

@author: Brandon Demeritt
'''
import math
#Prompt user for wall height and width

wallHeight = float(input("Please enter the height of the wall in feet: "))
wallWidth = float(input("Please enter the width of the wall in feet: "))

#Calculate and show wall area

wallArea = int(wallHeight) * int(wallWidth)
print("\nThe walls area is: ", wallArea)

#Calculate gallons of paint needed to paint wall

gallonsNeeded = float(wallArea / 350)
print("\nYou need %f gallons of paint for this wall."% gallonsNeeded)

#Calculate number of 1 gallon cans needed.

intGallonsNeeded = math.ceil(gallonsNeeded)
print(f"You need to purchase {intGallonsNeeded} gallon(s) to paint this wall.")

#Ask for color, output total cost of paint depending on color

colorCost = {
    "Red" : 35,
    "Blue" : 25,
    "Green" : 23
}

userColor = input("\nPlease input which color you want to use (Red, Blue or Green): ")
totalCost = colorCost[userColor] * intGallonsNeeded
print(f"\nTotal cost to paint with this color: ${totalCost}")

print("\nThe End")