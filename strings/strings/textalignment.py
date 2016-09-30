thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cones of two verical lines
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))    #printing two lines of specified thickness and middle with space in incrementing order

#Top vertical lines
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))  #printing two lines of specified thickness and middle with space

#Middle line joining two lines
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    # horizontal with extreme length

#Bottom vertical lines
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    #printing two lines of specified thickness and middle with space

#Inverted Bottom Cones of two vertical lines
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))   #printing two lines of specified thickness and middle with space in decrementing order
