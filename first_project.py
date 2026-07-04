# BANK MANAGEMENT PROJECT

import random
import json
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fp:
                data=json.loads(fp.read())
    except Exception as err:
        print(f"Error Occured As {err}")
    
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fp:
            fp.write(json.dumps(Bank.data))

    @staticmethod
    def __accountgeneration():
        ch=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=4)
        sp=random.choices("@#$%^&*!~",k=1)
        id=ch+num+sp
        random.shuffle(id)
        return "".join(id)
    
    @classmethod
    def createaccount(cls):
        info={
            "name":input("Enter Your Name:"),
            "age":int(input("Enter Your Age:")),
            "email":input("Enter Your Email:"),
            "contact":int(input("Enter Your Mobile Number:")),
            "pin":int(input("Enter Your Pin:")),
            "marital_status":input("Enter Your Marital Status:"),
            "accountno.":Bank.__accountgeneration(),
            "balance":0,

        }
        if info["age"]<18 or len(str(info["pin"]))!=4 or len(str(info["contact"]))<10:
            print("Sorry You Cannot Have A Bank Account!\nor\nThe Pin is Invalid!\nor\nThe Phone Number is Invalid!")
        else:
            print("Congratulations,Your Bank Account Has Been Created Succesfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            Bank.data.append(info)
            Bank.__update()
    
    @classmethod
    def deposit_money(cls):
        account=input("Enter Your Account Number:")
        pin=int(input("Enter Your Pin:"))

        userdata=[i for i in Bank.data if i['accountno.']==account and i['pin']==pin]
        if not userdata:
            print("Sorry,No Such Record Found!")
            return

        amount=int(input("Enter Amount to be Deposited ==> "))
        if amount>100000 or amount<0:
            print("Amount is exceeding the limit or you are entering 0!")
            return

        userdata[0]['balance']+=amount
        Bank.__update()
        print("Amount Has Been Deposited Successfully!")
    
    @classmethod
    def withdraw_money(cls):
        account=input("Enter Your Account Number:")
        pin=int(input("Enter Your Pin:"))

        userdata=[i for i in Bank.data if i['accountno.']==account and i['pin']==pin]
        if not userdata:
            print("Sorry,No Such Record Found!")
            return

        amount=int(input("Enter Amount to be Withdrawn ==> "))
        if amount>userdata[0]['balance']:
            print("Insufficient Balance!")
            return

        userdata[0]['balance']-=amount
        Bank.__update()
        print("Amount Has Been Withdrawn Successfully!")
    
    @classmethod
    def show_details(cls):
        account=input("Enter Your Account Number:")
        pin=int(input("Enter Your Pin:"))

        userdata=[i for i in Bank.data if i['accountno.']==account and i['pin']==pin]
        if not userdata:
            print("Sorry,No Such Record Found!")
            return

        print("Your Bank Account Details are:")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    @classmethod
    def update_details(cls):

        account=input("Enter Your Account Number:")
        pin=int(input("Enter Your Pin:"))

        userdata=[i for i in Bank.data if i['accountno.']==account and i['pin']==pin]
        if not userdata:
            print("Sorry,No Such Record Found!")
            return

        newdata={
            "name":input("Enter Name or Enter to Skip :"),
            "email":input("Enter Email or Enter to Skip :"),
            "contact":input("Enter New Contact or Enter to Skip :"),
            "marital_status":input("Enter Your Marital Status or Enter to Skip :")

        }
        if newdata["name"]=="":
            newdata["name"]=userdata[0]['name']
        if newdata["email"]=="":
            newdata["email"]=userdata[0]['email']
        if newdata["contact"]=="":
            newdata["contact"]=userdata[0]['contact']
        else:
            newdata["contact"]=int(newdata["contact"])
        if newdata["marital_status"]=="":
            newdata["marital_status"]=userdata[0]['marital_status']

        newdata["age"]=userdata[0]['age']
        newdata["pin"]=userdata[0]['pin']
        newdata["accountno."]=userdata[0]['accountno.']
        newdata['balance']=userdata[0]['balance']

        for i in newdata:
            if newdata[i]==userdata[0][i]:
                continue
            else:
                userdata[0][i]=newdata[i]

        print("Your New Updated Bank Details are:")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

        Bank.__update()

    def delete_account(self):
        account=input("Enter Your Account Number:")
        pin=int(input("Enter Your Pin:"))

        userdata=[i for i in Bank.data if i['accountno.']==account and i['pin']==pin]
        if not userdata:
            print("Sorry,No Such Record Found!")
            return
        last=input("Are you Sure You want to Delete your Bank Account,Press Y/y for Deleting your Bank Account ==>")
        if last=='y' or last=='Y':
            Bank.data.remove(userdata[0])

            print("Your Bank Account Has Been Deleted Succesfully!")

            Bank.__update()


            


        

if __name__ == "__main__":
    user=Bank()

    print("Press 1 for Opening An Account:")
    print("Press 2 for Deposting Money:")
    print("Press 3 for Withdrawing Money:")
    print("Press 4 for Showing the Account Details:")
    print("Press 5 for Updating the Account Details:")
    print("Press 6 for Deleting the Account:")

    while True:
        choice=int(input("Enter Service You Want to Acess:"))
        if choice==1:
            user.createaccount()
        if choice==2:
            user.deposit_money()
        if choice==3:
            user.withdraw_money()
        if choice==4:
            user.show_details()
        if choice==5:
            user.update_details()
        if choice==6:
            user.delete_account()
        ch=input("DO YOU WANT TO CONTINUE Y/N ==> ")
        if ch=='n' or ch=='N':
            break
    print("Thank You! Have A Nice Day.")




