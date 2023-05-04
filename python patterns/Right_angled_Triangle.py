num = int(input("Enter the number: "))
for row in range(1, num+1, 2):
    for col in range(1, row+1):
        print("*", end="")
    print()
