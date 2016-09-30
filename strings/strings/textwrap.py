import textwrap
s=raw_input()
i=int(raw_input())
for x in range(0,len(s),i):  #ranging the string with length and wrapping leangth
    print s[x:x+i]   #printing the value with wrapped length of values in the array of string
