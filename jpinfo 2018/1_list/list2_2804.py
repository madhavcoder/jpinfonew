#Program : Noraml List with append and remove
#Author  : Madhavv j
#Date    :28 04 2018

import os
x=[1,2,4]
print (x)

print ("After apend 9")
x.append(9)
print (x)

print ("After remove 2")
x.remove(2)
print (x)

x.remove(0)   #it will show you valueerror:x not in list
print (x)