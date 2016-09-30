s =raw_input()
for x in s[:].split():   #spliting the string into array character of strings
    s = s.replace(x, x.capitalize())   #every string character is capitalised and replaced
print s
