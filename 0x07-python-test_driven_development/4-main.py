#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print_square()
try:
    print_square(-4)
except Exception as e:
    print(e)
print("")

try:
    print_square(4.6)
except Exception as e:
    print(e)
print("")

try:
    print_square(-4.6)
except Exception as e:
    print(e)
print("")

try:
    print_square()
except Exception as e:
    print(e)
print("")

try:
    print_square("hello")
except Exception as e:
    print(e)
print("")