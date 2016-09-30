from itertools import combinations_with_replacement    #importing the combinations with replacements package from itertools
x,n=raw_input().split(" ")    
list1 = list(combinations_with_replacement(x,int(n)))   #performing the combination with replacement into a list
a = []   #initialising 2 empty list
list2 = []
for i in range(len(list1)):
    list2.append(list(list1[i]))    #appending the list into another list
list3 = []
for i in range(len(list2)):
    list2[i].sort()   #sorting the list
for i in range(len(list2)):
    a.append(''.join(map(str,list2[i])))    #appending the list2 to list a 
a.sort()   #sorting the list
for i in range(len(a)):
    print a[i]   #printing the elements in the list
