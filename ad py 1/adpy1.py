class Car:
    status="idle"
    def __init__(self,brand, year):
        self.brand=brand
        self.year= year
    def run(self):
        self.status="Running"


# doi tuong(object)

car1=Car("huyndai",1960)

print(car1.brand)


# car1.run()
# print(car1.status)


# class Counter:
#     count=0
#     def __init__(self,hour=0, minute=0,second=0):
        
#         self.hour=hour
#         self.minute=minute
#         self.second=second
        
#     def tick(self):
#         self.second+=1
#     def reset(self):
#         self.hour=0
#         self.minute=0
#         self.second=0
#     def hour(self):
#         return self.hour
#     def minutes(self):
#         return self.minute
#     def second(self):
#         return self.second

# A=Counter()
# print(A.count)
# A.tick()
# print(A.count)
# A.reset()
# print(A.count)

# class Timer:
#     def __init__(self,constructor=0):
#         self.constructor=constructor
#     def tick(self):
#         self.constructor+=1

li=[1,2,3,4,5]
a=0
for i in range(len(li)):
    a+=1
    newLi=li[a]+1
print(newLi) 
    
