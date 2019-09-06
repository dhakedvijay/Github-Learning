from pickle import load,dump
import os
class bank():
    def check(self):
        try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
        except EOFError:
            self.acc_no=t.acc_no+1
                
        except FileNotFoundError:
            self.acc_no=635124225100
            file=open("Bankin.bin","wb")
        file.close()



    def create(self,t1,t2,t4):
        self.check()
        self.name=t1
        while True:
            self.t=t2
            if self.t not in ('S','C'):
                print("Invalid type of account")
            else:
                break
        
        print("your account no is: ",self.acc_no)
        
        while True:
            self.ammount=t4
            if self.t=='S' and  int(self.ammount)<5000:
                print("Sorry we can't open your account:\n Choose a valid ammount:")
            elif self.t=='C' and int(self.ammount)<10000:
                print("Sorry we can't open your account:\n Choose a valid ammount:")
            else:
                break
        file=open("Bankin.bin","ab")
        dump(self,file)
        file.close()
        return self.acc_no

        '''try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
        except EOFError:
            print("{:<25}{:<15}{:<15}{:<15}".format("Acc_No","Name","Type","Balence"))
            print("{:<25}{:<15}{:<15}{:<15}".format(t.acc_no,t.name,t.t,t.ammount))
        file.close()'''

#view all
    def viewall(self):
        try:
            l=[]
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
                l.append(str(t.acc_no)+'  '+t.name+'  '+t.t+'  '+str(t.ammount))
        except EOFError:
            pass
        file.close()
        return l

#search account
    def search(self,t3):
        acc=int(t3)
        try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    l=[t.acc_no,t.name,t.t,t.ammount]
                    file.close()
                    return str(t.acc_no)+'  '+t.name+'  '+t.t+'  '+str(t.ammount)
     
        except EOFError:
            pass
        file.close()


#Update Account
    def update(self,t1,t3):
        acc=int(t3)
        nam=t1
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    t.name=nam
                dump(t,file1)
        except EOFError:
            pass
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        

        
#Deposite
    def Deposit(self,an,am):
        acc=int(an)
        amm=int(am)
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    t.ammount=int(t.ammount)+amm
                dump(t,file1)    
        except EOFError:
            print("Account not found")
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        

        
#Withdraw
    def withdraw(self,an,am):
        acc=int(an)
        amm=int(am)
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    t.ammount=t.ammount-amm
                dump(t,file1)    
        except EOFError:
            print("Account not found")
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        
        

        







'''while True:    
    print("New Account: 1")
    print("Display: 2")
    print("Add Money: 3")
    print("Withdraw: 4")
    print("Update name: 5")
    print("search account: 6")
    print("Exit: 7")
    n=int(input("enter your choice: "))
    b=bank()
    if n==1:
        b.create()
    elif n==2:
        b.viewall()
    elif n==3:
        b.deposit()
    elif n==4:
        b.withdraw()
    elif n==5:
        b.update()
    elif n==6:
        b.search()
    else:
        break
    
'''    
