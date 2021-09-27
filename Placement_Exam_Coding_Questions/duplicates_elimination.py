arr=[1,4,2,5,2,3,4,5,1,2,3]

# Using Set function

arr2=list(set(arr))
print("Removed by Set()\n",arr2)

# Using Array
arr3=[]

for i in arr:
    if i not in arr3:
        arr3.append(i)
print("",arr3)

# Using Lambda function
rem_duplicate_func=lambda arr:set(arr)
print("",list(rem_duplicate_func(arr)))