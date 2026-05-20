import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occured as {err}")
        
        
    @classmethod
    def __update(cls):
        try:
            with open(cls.database,'w') as fs:
                fs.write(json.dumps(cls.data))
        except Exception as err:   
            print(f"An exception occured as {err}")
    
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)           
       
        
                
    
    def create_account(self):
        info={
            "name":input("Enter your name: "),
            "age":int(input("Enter your age: ")),
            "email":input("Enter your email:" ),
            "pin":int(input("Enter your pin: ")),
            "account_No":Bank.__accountgenerate(),
            "balance":0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create your account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please remember your account number and pin for future use")
            Bank.data.append(info)
            Bank.__update()


    def deposit(self):
        accnumber=input("Please enter your account number: ")
        pin=int(input("Please enter your pin: "))
        userdata=[i for i in Bank.data if i['account_No']==accnumber and i['pin'] == pin ]
        
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much do you wanna deposit: "))
            if amount>10000 or amount <0:
                print("Sorry the amount is too much, You can deposit below 10000")
            else:
                userdata[0]["balance"]+=amount
                Bank.__update()
                print("Amount deposited successfully")
                print(userdata)
                print("closing Statement")
                
    def withdraw(self):
        accnumber=input("Please enter your account number: ")
        pin=int(input("Please enter your pin: "))
        userdata=[i for i in Bank.data if i['account_No']==accnumber and i['pin'] == pin ]
        
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much do you wanna withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry you dont have that much money")
            else:
                userdata[0]["balance"]-=amount
                Bank.__update()
                print("Amount withdrewn successfully")
                print(userdata)
                print("Closing Statement")
        

user=Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money from the bank")
print("Press 4 for checking the details of the account")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")

check=int(input("Enter your response: "))

if check==1:
    user.create_account()
elif check==2:
    user.deposit()
elif check==3:
    user.withdraw() 
    