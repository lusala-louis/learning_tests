def inputGrades(totalGrades):
    yourGrades=[]
    i=0
    while(i<totalGrades):
        grades=float(input('Enter Your Grades: '))
        yourGrades.append(grades)
        i=i+1
    return yourGrades
def printGrades(grades):
    print('Your Grades Are: ',myList)
def avgGrades(grades):
    sumGrades=0
    for grade in range(0,numGrades,1):
        sumGrades=sumGrades+grades[grade]
    avgGrades=sumGrades/numGrades
    print('The average grade is: ',round(avgGrades,2))   
    return avgGrades
def highLow(grades,gradesArray):
    for grade in range(0,numGrades-1,1):
        for grade in range (0,numGrades-1,1):
             if (gradesArray[grade]<gradesArray[grade+1]):
                 swp=gradesArray[grade]
                 gradesArray[grade]=gradesArray[grade+1]
                 gradesArray[grade+1]=swp
    print('Your Sorted Grades List is: ')
    for grade in range(0,numGrades,1):
        print(gradesArray[grade])
    return gradesArray
numGrades=int(input('How Many Grades Do you have? '))
myList=inputGrades(numGrades)
printGrades(myList)
average=avgGrades(myList)
gradeList=highLow(numGrades,myList)