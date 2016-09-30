n = int(input())
s = set(map(int,raw_input().split()))
b = int(input())
a = set(map(int,raw_input().split()))
x=set(s).intersection(a)   #making the intersection of the two sets
count=0
for i in x:
    count=count+1   #counting the elements in the intersection set
print count
