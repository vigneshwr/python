from itertools import combinations   #importing combinations package from itertools
x,n=raw_input().split(" ")
for i in range(1, int(n)+1):
    for j in list(combinations(sorted(x),i)):    #performing combinations for the sorted list of the elements from the input
        print ''.join(j)    #printing the list of elements in a single line
