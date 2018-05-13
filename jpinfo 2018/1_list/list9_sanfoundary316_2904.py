#program:Python Program to Remove the Duplicate Items from a List
##Author  : Madhavv j
#Date    :29 04 2018

import os

x=[1,4,5,5,6,7,8,9,0,9,5,9]

l=len(x)
i=j=0
a=[]
while i<=l:
	j=i
	while j<=l:
		if x[j] not in a:
			a.append(x[i])
		j=j+1
	i=i+1

print(a)	





