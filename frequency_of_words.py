# Count the frequency of words appearing in a string

def frequency_counter():
    str = input("Enter a String")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
    print(d)


frequency_counter()
