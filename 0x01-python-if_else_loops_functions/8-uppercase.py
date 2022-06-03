#!/usr/bin/python3
str = ""
def uppercase(str):
	for i in str:
		if ord(i) >= 97 and ord(i) <= 122:
			i = ord(i)-32
		str += chr(i)
	print('{:s}'.format(str))
