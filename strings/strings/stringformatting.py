STDIN = int(raw_input())
w = len(str(bin(STDIN)).replace('0b',''))

for i in xrange(1, STDIN+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')    #converting the input to binary format
    o = oct(int(i)).replace('0','', 1).rjust(w, ' ')  #converting the input to octal format
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')   #converting the input to hexadecimal format
    j = str(i).rjust(w, ' ')
    print j, o, h, b
