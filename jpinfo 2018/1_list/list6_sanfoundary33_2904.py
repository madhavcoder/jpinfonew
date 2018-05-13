#Program :Python Program to Put Even and Odd elements in a List into Two Different Lists
#Author  : Madhavv j
#Date    :29 04 2018


import os
x=[23,20,3,4,5,6,7,-1]
i=0
tempmax=0
tempodd=[]
tempeven=[]


for i in x:
	if i%2==0:
		tempeven.append(i)
	else:
		tempodd.append(i)


print ("Odd List is",tempodd)
print("Even list is",tempeven)


