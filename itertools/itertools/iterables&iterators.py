from itertools import combinations;   #import combinations package from itertools
l = int(input().strip());
s = input().strip().split();
k = int(input().strip());

good = 0;
all=0;
for i in combinations(s,k):
	all+=1;    #calculating the possible combination's count
	if 'a' in i:
		good=good+1;    #finding the count of the char
		
print(good/all);   #printing the probability 
