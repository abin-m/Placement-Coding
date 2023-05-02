def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the limit:"))
result=fib(n)
print("The Result=",result,"\n")