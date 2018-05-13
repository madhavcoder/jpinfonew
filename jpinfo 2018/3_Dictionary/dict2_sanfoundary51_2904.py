#Python Program to Concatenate Two Dictionaries Into One
#Name :
#Date:
import os
dictx={'a':1,'b':2}
dicty={'f':4,'g':8,'h':0}
dictz={}

dictz = dict(dictx.items() + dicty.items())   #only supports nin pythion2 so runse in python2 only
#dictz=dictx.push(dicty)#+dicty
print (dictz)



#second way to do
print "second way using udpate method"
dall = {}
for d in [dictx, dicty]:
  dall.update(d)
print dall