n = int(input())
s = set(map(int,raw_input().split()))
b = int(input())
a = set(map(int,raw_input().split()))
x=set(s).difference(a)   #making the difference of the two sets
count=0
for i in x:
    count=count+1   #finding the count of the difference set
print count
