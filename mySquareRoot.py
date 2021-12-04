def squareRoot(num):
    root=0
    i=0
    while(i<num): #for i in range(0,num,1):
       if (num==i*i):
           root=i
       i=i+1
    return root
j=0
while(1==1):
    num=float(input('Please Enter a Number: '))
    if (num>0):
        answer=squareRoot(num)
        print(answer)
        print('You can always press zero to exit.')
    elif (num<=0):
        print('Only Works With Numbers Greater Than Zero.')
        break
    j=1