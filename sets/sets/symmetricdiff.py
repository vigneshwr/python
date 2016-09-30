input()
a=set(map(int,raw_input().split()))   #initialising a set,mapping input values
input()
b=set(map(int,raw_input().split()))   #initialising a set,mapping input values
c=a.symmetric_difference(b)   #finding the symmetric difference between two sets of values
for n in sorted(list(c)):   #sorting the list of values
    print n
