#Program : Noraml 2D List with append and remove
#Author  : Madhavv j
#Date    :28 04 2018

import os
x=[[1,2,4],[1,2,5],[2,3,4]]
print (x)

print ("printing x[0] element")
print (x[0])

print("printing x[0][1] element")
print (x[0][1])

print ("After apend 9")
x.append(9)
print (x)

print ("After apend [2,4]")
x.append([2,4])
print (x)

print ("Again After apend 9")
x.append(9)
print (x)

print ("After remove 9")  #see ourput in end 9 remains
x.remove(9)
print (x)

print ("Again remove 9")  #see output no 9 is there
x.remove(9)
print (x)


