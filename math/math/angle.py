import math    #importing math package
AB = int(raw_input())    #input the length of two sides
BC = int(raw_input()) 
print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'    #finding the angle betweentwo sides by calculating the tan angle rounding off to integer
