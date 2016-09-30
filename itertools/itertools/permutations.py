from itertools import permutations   #importing permutation packge from itertools
x=raw_input().split(" ")
p=list(permutations(x[0],int(x[1])))    #performing permutations of the two arguments of the input
for i in sorted(p):
    print ''.join(i)   #joining the elements in a single line in a sorted order
