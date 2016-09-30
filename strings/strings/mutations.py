string=raw_input()
l=list(string)   #creating a list of string inputs 
i,c=raw_input().split()
string=string[:int(i)]+c+string[int(i)+1:]  #performing a mutation of the string with the value given as input
print string
