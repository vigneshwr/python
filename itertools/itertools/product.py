from itertools import product   #import product package from itertools package
a=map(int,raw_input().split())
b=map(int,raw_input().split())

ans=[a,b]   #formatting the input values into a set values
c=list(product(a,b))    #calculating the product of two sets into a list
for i in c:
    print i,   #printing the elements of the list in a single line
