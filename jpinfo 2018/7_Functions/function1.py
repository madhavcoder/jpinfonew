#Program : Noraml Function Program
#Author  : Madhavv j
#Date    :28 04 2018



import os

def summation(x,y):
	print("Summation of",x,"and",y,"is")
	return x+y

def subtraction(x,y):
	print("Subtraction of",x,"and",y,"is")
	return x-y

def multiplication(x,y):
	print("Multiplication of",x,"and",y,"is")
	return x*y

def division(x,y):
	print("Division of",x,"and",y,"is")
	return x/y

#Driverr Code
#if __name__=='__main()__'
print(summation(5,6))

print(subtraction(36,5))

print(multiplication(6,5))

print(division(45,5))