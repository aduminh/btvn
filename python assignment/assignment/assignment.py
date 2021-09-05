
from random import randint

def new_account():
    dic={}
    name= input("enter your name")
    dic['name']=name
    address= input("enter your address")
    dic['address']=address
    phone= input("enter your phone number")
    dic['phone']=phone
    initial= int(input("enter your initial"))
    dic['initial']=initial
    password= input("enter your password")
    repassword= input("reenter your password")
    account_number= randint(0,100000)
    dic['account_number']=account_number
    while repassword!=password:
        print("Password confirmation and password must be the same")
        password=input("enter your password")
        repassword=input("reenter your password")
    dic['password']=password
    print("Your account has been successfuly completed as:")
    return dic

    
    
def display(dic):
    print('Name:'+dic['name'])
    print('address:'+dic['address'])
    print('phone:'+dic['phone'])
    print('initial:'+dic['initial'])
    print('account number:'+dic['account_number'])

def change_password(dic):
    newpassword= input("enter your new password")
    retypepassword=input('reenter new password')
    while retypepassword!=newpassword:
        print("Password confirmation and password must be the same")
        newpassword=input("enter your password")
        retypepassword=input('reenter new password')
    dic['password']=newpassword

    
        
    
