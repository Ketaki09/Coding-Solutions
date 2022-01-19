import math
#Get user input for 2 sides of the triangle.
#sides AB, BC
AB = int(input())
BC = int(input())

#Use pythagoras theorem to calculate height of hypothenuse
temporaryValue = pow(AB, 2) + pow(BC, 2)
AC = round(pow(temporaryValue, 0.5),2)

#angle ACB is equal to angle MBC
angleC = round(math.degrees(math.asin(AB/AC)))

# u'\xb0' is the Unicode required for the getting the degree symbol in the end
angleC = str(angleC)+ str(u'\xb0')
print(angleC)