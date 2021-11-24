def  tally(totalNum,numArray):
    sum=0
    for i in range(0,totalNum,1):
         sum=sum+numArray[i]
    return sum
totalNum=4
numArray=[]
for i in range(0,totalNum,1):
    num=float(input('Enter a Number: '))
    numArray.append(num)
c=tally(totalNum,numArray)
print('The sum is ',c)