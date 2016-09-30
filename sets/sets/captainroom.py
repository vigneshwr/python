 k,arr = int(raw_input()),list(map(int,raw_input().split()))    #getting inputs as in array
myset = set(arr)    #pulling the array into a set
print ((sum(myset)*k)-(sum(arr)))//(k-1)   #finding the odd k-unrepeating element in the set
