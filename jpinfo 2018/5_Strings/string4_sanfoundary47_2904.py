#Python Program to Calculate the Length of a String Without Using a Library Function
#Date:29 04 2018

import os

s=input("Please Enter Any String:")
i=temp=0

while (s[i]!=0):
	temp=temp+1
	i=i+1

print(temp)