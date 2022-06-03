#!/usr/bin/python3
def uppercase(str):
	newstr = ""
	for i in str:
		if ord(i) >= 97 and ord(i) <= 122:
			i = ord(i)-32
		newstr += chr(i)
	print('{:s}'.format(newstr))
