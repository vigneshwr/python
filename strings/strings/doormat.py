N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print ((i*".|.").center(M,"-"))    #printing the string at the centre following the pattern
print ("WELCOME".center(M,"-"))   #printing the centre with centre alignment with other spaces with -
for i in range(N-2,-1,-2):    #for the range of vertical length below the mid line
    print ((i*".|.").center(M,"-"))   #printing the string at the centre following the pattern
