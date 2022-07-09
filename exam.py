print("----------------MENU---------------")
print("press 1 to creat exam details of subject")
print("press 2 to read details exams")
print("press 3 to update details of particular subject")
print("press 4 to retrive details of particular subject")
print("press 5 to delete details of particular subject")
print("press 6 to exit")
class exam:
            def getexamDetails(self):
                self.no=int(input("Enter subject number : "))
                self.subname = input("Enter subject Name : ")
                self.maxmarks =int(input("Enter Marks : "))
                self.questions=int(input("Enter total questions : "))
                self.result=input("Enter result-(pass or fail) : ")
            def printDetails(self):
                print(self.no,self.subname, self.maxmarks, self.questions,self.result)
            def get_no(self):
                return self.no
temp=[]
def find(val):
    for i in temp:
        if(i.get_no()==val):
            return i
def retirve():
    for i in temp:
        i.printDetails()
def delete(val):
    for i in temp:
        if(i.get_no()==val):
            temp.remove(i)
def modify(val):
    print("----------------MENU---------------")
    print("1.subject number")
    print("2.subname")
    print("3.maxmarks")
    print("4.number of questions")
    print("5.result")
    n=int(input("enter field id  to modify :"))
    for i in temp:
         if(i.get_no()==val):
            new=input("enter new value : ")
            if(n==1):
                i.no=int(new)
            elif(n==2):
                i.subname=new
            elif(n==3):
                i.maxmarks=int(new)
            elif(n==4):
                i.questions=int(new)
            else:
                i.result=new
            break
for i in range (1,100):
    a=int(input("enter the operation:-"))
    e1=exam()           
    if a==1:
        e1.getexamDetails()
        temp.append(e1)
    elif a==2:
            retirve()
    elif a==3:
        val=int(input("enter subject number to modify :"))
        modify(val)
    elif a==4:
        val=int(input('enter subject number : '))
        st=find(val)
        st.printDetails()
    elif a==5:
        val=int(input("enter subject number to delete :"))
        delete(val)
    else:
        break
