feet = float(input('Enter the distance in feet:'))
inches = float(input('Enter the distance in inches:'))

#Formula to convert to meters
meters =(feet * 0.3048) + (inches * 0.0254)

#Formula to convert to centimeters 
centimeters = meters * 100

print('Distance in meters =',meters)
print('Distance in centimeters =',centimeters)