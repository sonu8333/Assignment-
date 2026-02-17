x = int(input('Enter a 3 digit number:'))

hundreds = x // 100
tens = (x // 10) %10
units = x % 10

total = hundreds + tens + units

print(hundreds)
print(tens)
print(units)
print('Sum of all digits:',total)