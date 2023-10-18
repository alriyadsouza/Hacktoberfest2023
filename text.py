#Accepting roll,name and marks of 3 subjects in a text file marks.txt and display name,total marks of all students.
f=open("Marks.txt","w")
n=int(input("How many no of students do you want to enter?"))
for i in range(n):
    L=[]
    r=input("Enter roll:")
    na=input("Enter name:")
    p=input("Enter physics marks")
    c=input("Enter chemistry marks")
    m=input("Enter maths marks")
    L=[r," ",na," ",p," ",c," ",m]
    f.writelines(L)
    f.writelines("\n")
f.close()

f=open("Marks.txt","r")
data=f.readline()
while data:
    Total=0
    data=data.split()
    Total=int(data[2])+int(data[3])+int(data[4])
    print("Name=",data[1],"Total=",Total)
    data=f.readline()
f.close()