list=[];   #creating an empty list
t=int(raw_input());
for i in range(0,t):
    x=raw_input().split();   #getting input from the user and splitting into array structure
    if x[0] == "insert":   
        list.insert(int(x[1]),int(x[2]))   #checks for INSERT operator and performs insertions
    elif x[0] == "append":
        list.append(int(x[1]))   #checks for APPEND operator and perform append operation
    elif x[0] == "pop":
        list.pop();  #checks for POP operator and performs pop operation
    elif x[0] == "print":
        print list   #checks for PRINT operator and prints the array
    elif x[0] == "remove":
        list.remove(int(x[1]))   #checks for the REMOVE operator snd performs remove operation
    elif x[0] == "sort":
        list.sort();  #checks for the SORT operator and performs sorting
    else:
        list.reverse();   #if not reverse it
