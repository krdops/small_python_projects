import math
import random


x = input("Enter amount of passwords: ")
x = int(x)
i = 0
ranlist = ["ainima", "togk", "gokto"]
fulllist = []
while i < x:
    i+=1
    z = random.randint(0, len(ranlist)-1)
    l = ranlist[z]
    
    fulllist.append(l + str(random.randint(100, 999)))



print (fulllist)
