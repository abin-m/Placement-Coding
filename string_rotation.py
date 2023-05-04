# Algo

# 1: Concatenate string with itself
# 2: Traverse the concatinated string from 0 to size -1
# 3: print all substrings

def lefRotatedString(name):
    size = len(name)

    temp = name + name

    for i in range(size):
        for j in range(size):
            print(temp[i+j], end="")
        print("")


string = "ABIN"

lefRotatedString(string)
