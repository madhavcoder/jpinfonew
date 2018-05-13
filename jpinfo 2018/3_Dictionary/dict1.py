#Program : Noraml Dictionary concepts
#Author  : Madhavv j
#Date    :28 04 2018

import os
dicta={'a':1,'b':2}
print (dicta)



print ("printing dict1 keys")
print (dicta.keys())

print("printing dicta values")
print (dicta.values())

print ("Dictionary a's value:")
print (dicta['a'])

print ("Udating with C value")
dicta['c']=3
print (dicta)

print ("remove entry done with b")
del dicta['b']
print (dicta)

print ("Remove all entries with dictionary and printing")
dicta.clear()
print (dicta)
