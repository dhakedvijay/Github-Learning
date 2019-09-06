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



    def create(self):
        self.check()
        self.name=input("Enter your full name: ")
        while True:
            self.t=input("Press 'S' for saving account and 'C' for current account: ")
            if self.t not in ('S','C'):
                print("Invalid type of account")
            else:
                break
        
        print("your account no is: ",self.acc_no)
        
        while True:
            self.ammount=int(input("Enter Ammount min. ammount is 5000 for saving and 10000 for current: "))
            if self.t=='S' and  self.ammount<5000:
                print("Sorry we can't open your account:\n Choose a valid ammount:")
            elif self.t=='C' and self.ammount<10000:
                print("Sorry we can't open your account:\n Choose a valid ammount:")
        
            else:
                break
        file=open("Bankin.bin","ab")
        dump(self,file)
        file.close()

        try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
        except EOFError:
            print("{:<25}{:<15}{:<15}{:<15}".format("Acc_No","Name","Type","Balence"))
            print("{:<25}{:<15}{:<15}{:<15}".format(t.acc_no,t.name,t.t,t.ammount))
        file.close()

#view all
    def viewall(self):
        print("All Account In Bank Are:")
        print("{:<25}{:<15}{:<15}{:<15}".format("Acc_No","Name","Type","Balence"))
        try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
                print("{:<25}{:<15}{:<15}{:<15}".format(t.acc_no,t.name,t.t,t.ammount))
        except EOFError:
            pass
        file.close()

#search account
    def search(self):
        acc=int(input("Enter account no: "))
        try:
            file=open("Bankin.bin","rb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    print("{:<25}{:<15}{:<15}{:<15}".format("Acc_No","Name","Type","Balence"))
                    print("{:<25}{:<15}{:<15}{:<15}".format(t.acc_no,t.name,t.t,t.ammount))
     
        except EOFError:
            pass
        file.close()


#Update Account
    def update(self):
        acc=int(input("Enter account no: "))
        nam=input("Enter new name")
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    t.name=nam
                dump(t,file1)
        except EOFError:
            print("Account not found")
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        self.viewall()


        
#Deposite
    def deposit(self):
        acc=int(input("Enter account no: "))
        amm=int(input("Enter ammount you want to deposit: "))
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    t.ammount=t.ammount+amm
                dump(t,file1)    
        except EOFError:
            print("Account not found")
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        self.viewall()

        
#Withdraw
    def withdraw(self):
        acc=int(input("Enter account no: "))
        amm=int(input("Enter ammount you want to withdraw: "))
        try:
            file=open("Bankin.bin","rb")
            file1=open("Dummy.bin","wb")
            while True:
                t=load(file)
                if acc==t.acc_no:
                    if t.ammount<amm:
                        file.close()
                        file1.close()
                        os.remove("Dummy.bin")
                        print("can not proceed")
                        return
                    
                    t.ammount=t.ammount-amm
                dump(t,file1)
        except EOFError:
            print("Account not found")
        file.close()
        file1.close()
        os.remove("Bankin.bin")
        os.rename("Dummy.bin","Bankin.bin")
        self.viewall()
        
        
        

        







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
