s = raw_input()

vowels = 'AEIOU'  #initialising vowels as inputs

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)  #checks for the occurance of vowels and adds it 
    else:
        stusc += (len(s)-i)   #checks for the non-occurance of vowel and adds it

if kevsc > stusc:
    print "Kevin", kevsc   #compares the counts and prints the highest as winner
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"   #if equal count,declared as draw
