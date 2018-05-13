#Program : Noraml String Program of reversings
#Author  : Madhavv j
#Date    :28 04 2018



import os

str1=input("Please Enter Any String:")
print (str1[::-1])


print ("replacing character in string:")
chr1=input("Please enter replace character you want:")
chr2=input("Please enter with character you want to replace:")
str2=str1.replace(chr1,chr2)
print(str2)