n = input()
A = set(map(int, raw_input().split())) 
N = input()
for _ in range(N):
    operator, M=raw_input().split()   #calling the operation and the operating inputs
    S = set(map(int, raw_input().split()))    #mapping the input into sets
    eval( "A.{operator}({value})"
    .format(operator=operator, value=repr(S) ) )   #performing the mentioned operation as in command line input
print sum(list(A))   #printing the list after operation
