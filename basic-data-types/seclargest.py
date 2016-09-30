i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]   #spliting the input values and mapping it to a list
z = max(lis)   #setting the max value of the list
while max(lis) == z:
    lis.remove(max(lis))  #removing the max value 

print max(lis)    # printing the max value (ie.printing the second largest value)
