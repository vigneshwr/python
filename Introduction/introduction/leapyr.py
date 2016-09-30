def is_leap(yr):   #defining a function to calculate the leap year
    
    if year % 400 == 0:   #checks for the divisibility by 400
        return "True"
    elif year % 100 == 0: #checks for the divisibility by 100
        return "False"
    elif year % 4 == 0:   #checks for the divisibility by 4
        return "True"
    else:
        return "False"    #else it is defined not a leap year 
n=int(raw_input())
print is_leap(n)  #calling the function
