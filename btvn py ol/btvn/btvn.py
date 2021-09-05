
def areaOfCircle(r):
    return r**2*3.14

def reverseString(s):
    return s[ : : -1]
a=input("enter")
print(reverseString(a))


def checkPalindrome(p):
    if p==p[ : : -1]:
        result=True
    if p!=p[ : : -1]:
        result=False
    return result
b=input("enter")
print(checkPalindrome(b))
