n = int(input())
s = set(map(int, input().split()))   #creating a set by mapping inputs 
t=int(input())
for i in range(t):
    c, *args = map(str,input().split())   #making command line arguments

    getattr(s,c) (*(int(x) for x in args))


print (sum(s))
