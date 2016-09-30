n = int(raw_input())
dic = {}   #creating dictionary
for l in range(n):
    i = raw_input().split(" ")  #spliting the raw input
    mark = map(float, i[1:])   #mapping the second half of input value into variable mark
    dic[i[0]] = sum(mark) / float(len(mark))   #performing average of the marks

print "%.2f" % round(dic[raw_input()],2)   #printing the dictionary rounding off to two digits
