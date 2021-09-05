class Employee:
    

    def __init__(self,name,position):
        self.name=name
        self.position=position

    

John=Employee("John","Engineer")  
def say_hi():
    print("Hello my name is"+John.name)
def tell_position():
    print("My position is"+John.position)
say_hi()
tell_position()

def calculate():
    a=input("Shape (rectangle/circle)")
    if a=="rectangle":
        w=int(input("width"))
        h=int(input("height"))
        s=str(w*h)
        p=str((w+h)*2)
        print("perimeter"+p)
        print ("square:"+s)
    elif a=="circle":
        r=int(input("r"))
        p=str(2*r*3.14)
        s=str(3.14*r**2)
        print("perimeter"+p)
        print ("square:"+s)
    else:
        print("invalid")
calculate()
# em khong hieu tao class o day la lam gi a
from datetime import datetime
now = datetime.now()

class CustomDate:
    def __init__(self,date=now.strftime("%d/%m/%Y"),time=now.strftime("%H:%M:%S")):
        self.date=date
        self.time=time
    def get_date(self):
        return self.date
    def get_time(self):
        return self.time

now = CustomDate()
print(now.get_date())
print(now.get_time()) 


