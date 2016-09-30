n=int(raw_input())  #reading integer input
t=tuple(map(int, raw_input().split()))   #splitting the input and mapping in the tuples
print hash(t)   #hashing func to hash the input value
