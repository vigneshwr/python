x,y,z,n = [input() for i in range(4)]   #reading four inputs 
print [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]   #printing the set of values of every value of x,y,z with sum not equal to 2
