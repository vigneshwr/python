n = int(input())
s = set(map(int,raw_input().split()))
b = int(input())
a = set(map(int,raw_input().split()))
x=set(s).symmetric_difference(a)   #finding the symmetric difference between the two sets 
count=0
for i in x:
    count=count+1   #calculating the remaining elements in the set
print count
