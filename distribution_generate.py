#!/usr/bin/python
import random
import string

while(1):
	pwdlim=input("pwd length: ")
	n=0
	char=""
	

	while pwdlim > n:
		s=str(random.choice(range(1,400)))
		char=char+s+" "
		n+=1
	print (char)
print("")
