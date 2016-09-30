from itertools import groupby    #importing the groupby package from itertools
x=map(int,raw_input())
for i,j in groupby(x):    #grouping the elements in the mapping input of list
    print (len(list(j)),i),    #printing the count of the element and the element
