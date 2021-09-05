def area_of_circle(r):
    return r**2*3.14
def perimeter_of_circle(r):
    return r*2*3.14
def area_of_rectangle(w,h):
    return w*h
def perimeter_of_rectangle(w,h):
    return (w+h)*2
def volume_of_sphere(r):
    return 4/3*3.14*r**3
def volume_of_rectangular_prism(w,l,h):
    return l*w*h
def main_function():
    while True:
        a= input("What do you want to calculate")
        if a.lower()=="quit":
            break
        elif a.lower()=="area":
            shape=input("What shape do you want to calculate")
            if shape.lower=="circle":
                r=float(input("nhap ban kinh"))
                area=area_of_circle
                print("The area of circle is"+ str(area))
            elif shape.lower=="rectangle":
                w=float(input("nhap width"))
                h=float(input("nhap height"))
                area=area_of_rectangle
                print("The area of rectangle is"+ str(area))
        elif a.lower()=="perimeter":
            perimeter=input("What shape do you want to calculate")
            if perimeter.lower()=="circle":
                r=float(input("nhap ban kinh"))
                perimeter=perimeter_of_circle
                print("The perimeter of circle is"+ str(perimeter))
            elif perimeter.lower()=="rectangle":
                w=float(input("nhap width"))
                h=float(input("nhap height"))
                perimeter=perimeter_of_rectangle
                print("The perimeter of rectangle is"+ str(perimeter))
        elif a.lower()=="volume":
            volume=input("What shape do you want to calculate")
            if volume.lower()=="sphere":
                r=float(input("nhap ban kinh"))
                volume=volume_of_sphere
                print("The volume of shpere is"+ str(volume))
            elif volume.lower()=="rectangular prism":
                w=float(input("nhap width"))
                h=float(input("nhap height"))
                l=float(input("nhap length"))
                volume=volume_of_rectangular_prism(w)
                print("The volume of rectangulare prism is"+ str(volume))
        else:
            print("invalid")
        
        
        
            
                



        
