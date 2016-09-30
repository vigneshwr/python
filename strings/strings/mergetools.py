S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):  #splits the string in N sized strings
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))   #adds it to the dictionary if the string has unrepeated set of characters
