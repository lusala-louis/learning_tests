numGrade=int(input('Please Enter The Number Of  Subjects You Take: '))
grades=[]
tempGrade=0
minGrade=100
maxGrade=0
previous=100
for i in range(0, numGrade, 1):
    grade=float(input('Please Enter Your Grade: '))
    grades.append(grade)
    print(grades)
print('Your Grades Are: ')
for i in range(0, numGrade, 1):
    print(grades[i])
sum = 0
for i in range(0, numGrade, 1):
    sum = sum + grades[i]
print('Your Total is: ', + sum)
average = sum / numGrade
print('Your Average is: ',+average)
for i in range(0, numGrade, 1):
    if(grades[i]> maxGrade):
        maxGrade=grades[i]
print(maxGrade, 'is the maximum')
for i in range(0, numGrade, 1):
    if(grades[i]< minGrade):
        minGrade=grades[i]
print(minGrade, 'is the minimum')
for i in range(0, numGrade-1, 1):
    for i in range(0, numGrade-1, 1):
        if (grades[i] < grades[i+1]):
            tempGrade=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=tempGrade
print('Your Sorted Grades Are: ')
for i in range(0, numGrade, 1):
    print(grades[i])