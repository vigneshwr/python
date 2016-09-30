import itertools    #import itertools package

k, m = map(int, raw_input().split())
lists= [map(int, raw_input().split())[1:] for i in range(k)]   #mapping the input to a list

s_max = []   #creating an empty list

for product in itertools.product(*lists):
	s_max.append(sum(map(lambda i: i**2, product))%m)   #finding the sum of the squares of the each element in each list

print max(s_max)  #printing the max value
