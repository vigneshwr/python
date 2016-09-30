i = input() 
j = set(input().split())   #input being split up and initialised in set
print(sum(int(i) for i in j)/len(set(j)))   #finding the average of all the values of the set
