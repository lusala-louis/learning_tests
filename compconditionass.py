number=float(input('Please Enter Your Number: '))
if(number%2==0 and number<0):
     print('Your number is a negative even number')
if(number%2==0 and number>0):
     print('Your number is a positive even number')
if(number%2==1 and number<0):
     print('Yournumber is a negative odd number')
if(number%2==1 and number>0):
    print('Your number is a positive odd number')
if(number==0):
    print('Your number is zero')