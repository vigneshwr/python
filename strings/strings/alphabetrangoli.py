import string
alpha = string.ascii_lowercase   #string alphabets as inputs

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])   #filling the free spaces with - symbol joining the string characters
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))   # appending the character from first to the nth alphabet
print('\n'.join(L[:0:-1]+L))   #joining the two strings
