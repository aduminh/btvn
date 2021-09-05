nums=(1,2,2,3,5,5,6,7,8,8)
def sum_of_unique_elements(nums):
    count={}
    
    for key in nums:
        count[key]=0
        if key in nums:
            count[key]+=1
    if count[key]==1:
        count[key]+=key
    else:
        count[key]+=0
print(sum_of_unique_elements(nums))
            
       
