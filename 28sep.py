a = int(input('Enter first number'))
b = int(input('Enter second number'))
c = int(input('Enter third number'))
greatest = 0
if a > b and b > c:
    greatest = a
if b > a and b > c:
    greatest = b 
if c > a and c > b:
    greatest = c
    print(greatest,"is the greatest of three number.")     
