n = int(input())
s = set(map(int, input().split()))   #creating a set by mapping inputs 
t=int(input())
for i in range(t):
    c, *args = map(str,input().split())   #making command line arguments

    getattr(s,c) (*(int(x) for x in args))   #performing all the operations in the arguments


print (sum(s))  #prints the sum of remaining elements in the set
