n, m = input().split()
arr = [int(x) for x in input().split()]   #initialising an array
A = set([int(y) for y in input().split()])   #generating sets
B = set([int(z) for z in input().split()])
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]   #counting the elements matching the sets A & B in array x
print(sum(count))    #printing the final count value
