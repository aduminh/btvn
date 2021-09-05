weekdays=[2,3,4,5,6]
# # tuple
# empty1st=[]
# emptytpl=()
# print(type(empty1st),type(emptytpl))
# info1st=[('name','Quan'),('name','Duc'),('age',21),('gender','male')]
# info=dict(info1st)

def dem(list1):
    count={}
    for key in list1:
        if key in count:
            count[key]+=1
        else:
            count[key]=1
    


