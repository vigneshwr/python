marksheet = []   #creating an empty list
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])   #reading the inputs and appending it into list

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]   #sorting the values and geting the second lowest values
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))   
