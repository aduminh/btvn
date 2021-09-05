b=-1
a =  input("nhap 1 so lon hon 10:")
while b< len(a):
    print(a[b])
    b-=1
c= int(input("nhap so du ban dau:"))  
d= int(input("nhap lai suat:"))
e= int(input("nhap so du mong muon"))
while c<e:
    print(c)
    c*=(1+d/100) 
    