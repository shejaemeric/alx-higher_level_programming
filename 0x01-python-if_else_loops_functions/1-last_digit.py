#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = int((str(number))[-1:])

if str > 5:
    print(f'Last digit of {number:d} is {str:d} and is greater than 5')
elif str == 0:
    print(f'Last digit of {number:d} is {str:d} and is 0')
else:
    print(f'Last digit of {number:d} is {str:d} and is less than 6 and not 0')    
