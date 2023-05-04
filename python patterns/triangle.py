num = int(input("Enter the number: "))
for row in range(1, num+1):
    for col in range(1, row+1):
        print("*", end="")
    print()

# second Triangle

for r in range(num, 0, -1):
    for c in range(1, r+1):
        print("*", end="")
    print()
