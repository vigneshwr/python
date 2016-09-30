for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i-1)//9)**2    #squaring the output of powers of 10 dividing by 9
#1*1=1
#11*11=121
#111*111=12321
#and so on
