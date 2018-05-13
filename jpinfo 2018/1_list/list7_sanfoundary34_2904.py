
#program:Python Program to Merge Two Lists and Sort it
#Author  : Madhavv j
#Date    :29 04 2018

import os

x=[1,4,3,2,95]
y=[5,5,6,7]

i=0
l=len(y)
#Merging List
while i!=l:
	x.append(y[i])
	i=i+1

print(x)


 
#Sorting List in ascending order
i=temp=0
l=len(x)
while i!=l:
	j=0    # if you change it to j=i ,it will be in descending order else acending order print

	#temp=x[i]
	while j!=l:
		if (x[i] <= x[j]):
			temp= x[i]
			x[i]=x[j]
			x[j]=temp
		j=j+1
	i=i+1

print (x)