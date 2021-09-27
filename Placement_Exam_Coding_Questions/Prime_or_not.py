from math import sqrt

def prime_num(num):
    if num>1:
        for i in range(2,int(sqrt(num))+1):
            if(num%i==0):
                return False
        return True
print("---------------PRIME OR NOT---------------\n")
flag=prime_num(int(input("Enter a Number:")))

if(flag):
    print("The Given number is PRIME")
else:
    print("The Given number is NOT A PRIME")

print("------------------------------------------")