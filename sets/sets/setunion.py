n = int(input())
s = set(map(int,raw_input().split()))
b = int(input())
a = set(map(int,raw_input().split()))
x=set(s).union(a)   #making the union of two sets
count=0
for i in x:
    count=count+1    #finding the count of elements in the union set
print count    
