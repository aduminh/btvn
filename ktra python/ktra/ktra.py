# Ho va ten: Pham Hung Minh
#Task 1:
def calc_sum(a, b):
    a=int(input("nhap so"))
    b=int(input("nhap so"))
    # hoi nguoi dung nhap so
    return a+b
    # tra ve tong
# print(calc_sum(1, 2))
# Task 2:
import math
def root_of_equation(a,b,c):
    a=int(input("nhap so dau khac 0"))
    b=int(input("nhap so thu 2 khac 0"))
    c=int(input("nhap so thu 3"))
    tamgiac=b**2-4*a*c
    if tamgiac>0:
        n1=(-b+math.sqrt(tamgiac))/2*a
        n2=(-b-math.sqrt(tamgiac))/2*a
        print("nghiem 1 la"+str(n1))
        print("nghiem 2 la"+ str(n2))
    elif tamgiac==0:
        n1=-b/2*a
        print("nghiem la" + str(n1))
    else:
        print("vo nghiem")
# root_of_equation(1,2,3)
# Task 3:
def number_of_char(n):
    num= str(n)
    return len(num)
# print(number_of_char(29436))
# Task 4:

def take_order():
    monan=[]
    while True:
    a=input("What do you want to eat")
    if a not in monan:
        monan.append("a")
        b=input("Do you want anything else(y/n)")
        if b=="y":
            continue
        if b=="n":
            break


    else:
        b=input("Do you want sth else, y or n")
        if b=="y":
            continue
        if b=="n":
            print("you have" )


# Task 5:

phone = {
    'Iphone12' : '28000000',
    'SamsungN10' : '16000000',
    'Oppo93' : '7500000',
    'Vsmart' : '7400000',
    'Vivo' : '4200000'
}

def get_price(phone_name):
    x = phone.get(phone_name)
    print(x)
get_price('Iphone12')
def get_suggestion(budget):
    list = []
    for x,y in phone.items():
        if int(y) <= budget:
            list.append(x)
    print(list)
get_suggestion(28000000)




    



    

