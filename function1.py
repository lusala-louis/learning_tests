def mathOp(x,y):
    add=x+y
    diff=x-y
    prod=x*y
    div=x/y
    return add,diff,prod,div
num1=float(input('Enter the First Number: '))
num2=float(input('Enter the Second Number: '))
addition,difference,multiplication,division=mathOp(num1,num2)
print('The sum is; ',addition)
print('The difference is ; ',difference)
print('The product is: ',multiplication)
print('The division is:',division)