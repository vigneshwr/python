A = set(map(int, raw_input().split()))   
N = int(raw_input())   
set_list = []   
for i in range(N):    #looping and appending the sets to a list
    x = set(map(int, raw_input().split()))
    set_list.append(x)
result = True
for i in set_list:    #iterating over the list, result will stay True as initialised, unless finding a set where A is not a superset.
    if not A.issuperset(i):
        result = False

print result
