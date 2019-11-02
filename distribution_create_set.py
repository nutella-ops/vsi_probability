#!/usr/bin/python
import random
import string

#create random number set to a file
file_out = open("rand_set.txt","w+")

#generate random number set
pwdlim=input("random set size: ")
n=0
char=""


while pwdlim > n:
    s=str(random.choice(range(1,400)))
    char=char+s+" "
    n+=1
#print (char)

file_out.write(char)
file_out.close()


