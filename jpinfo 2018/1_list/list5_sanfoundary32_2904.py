#Program :Python Program to Find the Second Largest Number in a List
#Author  : Madhavv j
#Date    :29 04 2018


import os
x=[23,20,3,4,5,6,7,-1]
i=0
tempmax=0
templist=[]
for i in x:
	if tempmax < i:
		tempmax=i
	else:
		templist.append(i)
#print(templist)
	
i=0
tempsecondmax=0
for i in templist:
	if tempsecondmax < i:
		tempsecondmax=i


print ("second maximum is",tempsecondmax)


#P.S   Please use this program with easiet complexity checking like kth number in c++