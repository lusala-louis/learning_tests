import pickle
numStudents=int(input('Enter the Number Of  Students in The Class: '))
students=[]
grades=[]
i=0
while(i<numStudents):
    student=input('Enter The Student Name :')
    students.append(student)
    grade=float(input('Enter Students Average Grade: '))
    grades.append(grade)
    i=i+1
with open('myGrades.pkl','wb') as f:
    pickle.dump(grades,f)
    pickle.dump(students,f)
with open('myGrades.pkl','rb') as g:
    a=pickle.load(g)
    b=pickle.load(g)
print(a)
print(b)
with open('myGrades.pkl','rb') as g:
    a=pickle.load(g)
    b=pickle.load(g)
while(1==1):
    name=input("Which Student's Grades Do You Want To Know? ")
    for i in range(0,numStudents,1):
        if students[i]==name:
            print(name,"'s Average Grade Is",grades[i])