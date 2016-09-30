s=raw_input()
print any(c.isalnum() for c in s)  #checks for alpha numeric characters
print any(c.isalpha() for c in s)  #checks for alphabets
print any(c.isdigit() for c in s)  #checks for the digits
print any(c.islower() for c in s)  #checks for lower case
print any(c.isupper() for c in s)  #checks for upper case
