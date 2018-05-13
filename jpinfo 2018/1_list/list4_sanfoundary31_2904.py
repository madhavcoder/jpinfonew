#Program :Python Program to Find the Largest Number in a List
#Author  : Madhavv j
#Date    :28 04 2018

import os
x=[23,3,4,5,6,7,-1]
i=0
tempmax=0
for i in x:
	if tempmax < i:
		tempmax=i
	
print("Maximum number is",tempmax)
