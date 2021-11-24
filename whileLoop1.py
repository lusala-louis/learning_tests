#Input And Print Out Grades
numGrades=int(input('Please Enter The Number Of Grades You Are Taking: '))
grades=[]
grade=0
j=1
while (j<=numGrades):
    grade=float(input('Enter your grade: '))
    grades.append(grade)
    j=j+1
print('Your Grades Are: ')
i=0
while (i<numGrades):
        print(grades[i])
        i=i+1
print(grades)   

