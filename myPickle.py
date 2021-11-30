import pickle
fruits=['apples','oranges','mangoes']
x=4
y=3.15
nuts=['almonds','groundnuts']
grades=[90,89,35,100]
dataSet=[fruits,x,y,nuts,grades]
#Creating file myData.pkl and loading data on to it
with open('myData.pkl', 'wb') as f:
    pickle.dump(dataSet,f)
    #pickle.dump(fruits, f)
    #pickle.dump(x, f)
    #pickle.dump(y, f)
    #pickle.dump(nuts, f)
    #pickle.dump(grades, f)
#Reading data from the myData.pkl file
with open('myData.pkl','rb') as g:
    a=pickle.load(g)
    #b=pickle.load(g)
    #c=pickle.load(g)
    #d=pickle.load(g)
    #e=pickle.load(g)
#Printing out the read data
print(a)
#print(b)
#print(c)
#print(d)
#print(e)
for data in a:
    print(data)

#Opening a file and reading from it
vehicles=['scooter\n', 'tuktuk\n', 'bike\n', 'car\n']
f=open('vehicles.txt','w+')      #Open a txt file called vehicles as a write file
f.writelines(vehicles)          #Load data into the file

 #Reading the data from the file
f=open('vehicles.txt')         
print (f.readlines())
f.close()