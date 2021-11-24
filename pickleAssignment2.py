import pickle
grades=[]
numStudents=4
students=[]
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
            print(str(name)+"'s Average Grade Is"+str(grades[i])+".")