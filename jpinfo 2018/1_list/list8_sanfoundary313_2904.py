#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
#Author  : Madhavv j
#Date    :29 04 2018

import random
i=0
x=[]

m=int(input("Enter How many numbers you want to Enter:"))

for i in range(m):
	x.append(random.randint(1,20))     # lear here regarding random fuctions
print(x)	