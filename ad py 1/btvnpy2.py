class Rectangle():
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def findArea(self):
        self.area=self.height*self.width
        return self.area
    def findPerimeter(self):
        self.perimeter=2*(self.height+self.width)
        return self.perimeter
    def __str__(self):
        return "Rectangle object with height = "+ str(self.height) + " and width = "+ str(self.width)
rect=Rectangle(2,1)
print(rect)

class MathList():
    def __init__(self,li):
        self.li=li
    def __str__(self):
        return str(self.li)
    def __add__(self,add_number):
        self.add_number=add_number
        result=[]
        for a in self.li:
            sum=a+self.add_number
            result.append(sum)
        return result
    def __sub__(self,subtract_number):
        self.subtract_number=subtract_number
        result=[]
        for b in self.li:
            subtract=b-self.subtract_number
            result.append(subtract)
        return result

li=MathList([1,2,3,4,5])
print(li)

li+=2
print(li)

class Square:
    def __init__(self,side):
        self.side=side
    def cal_area(self):
        area=self.side*self.side
        return area
class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
    def cal_area(self):
        return super().cal_area()*6
    def cal_volume(self):
        volume=self.side**3
        return volume
square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())


        
    





