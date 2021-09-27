num=int(input("Enter a Number:"))
x=num
n=len(str(num))
sum=0

while(num>0):
    r=num%10
    sum=sum+r**n
    num=num//10

if(x==sum):
    print("AMSTRONG")
else:
    print("NOT AN AMSTRONG")