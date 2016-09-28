n = int(raw_input())
if n % 2 == 1:
    print "Weird"  #checks for odd nos and print weird
elif n % 2 == 0 and 2 <= n <= 5:
    print "Not Weird"  #checks for even nos between 2 and 5 
elif n % 2 == 0 and 6 <= n <= 20:
    print "Weird"   #checks for even nos between 6 to 20
else:
    print "Not Weird" #for nos greater than 20 and if even
