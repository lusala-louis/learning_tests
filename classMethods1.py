class Student:
    def __init__(self,a,b):
        self.firstName=a
        self.secondName=b
        self.totalGrades=int(input('How Many Grades does the student have? '))
        #self.grades=[]
    def grades(self):
        self.grades=[]
        for grade in range(0,self.totalGrades,1):
            self.grade=float(input('Enter Your Grade: '))
            self.grades.append(self.grade)
        print(self.firstName ,self.secondName ,'has these grades: ',self.grades)
        return self.grades
    def average(self):
        sum=0
        for grade in range(0,self.totalGrades,1):
            sum=sum+self.grades[grade]
        self.avg=sum/self.totalGrades
        print(self.firstName ,self.secondName ,'has an average grade of: ',self.avg)
        return self.avg
    def maxMin(self):
        self.maxGrade=0
        for grade in range(0,self.totalGrades,1):
            if (self.grades[grade]>self.maxGrade):
                self.maxGrade=self.grades[grade]
        self.minGrade=100
        for grade in range(0,self.totalGrades,1):
            if (self.grades[grade]<self.minGrade):
                self.minGrade=self.grades[grade]
        print(self.firstName ,self.secondName ,'has the maximum grade of: ',self.maxGrade)
        print(self.firstName ,self.secondName ,'has the least grade of: ',self.minGrade)
        return self.maxGrade,self.minGrade
student1=Student('Lusala','Louis')
student1.grades()
print(' ')
student1.average()
print(' ')
student1.maxMin()
print(' ')
