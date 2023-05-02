# Find the common letters between 2 strings

def common_letters():
    str1 = input("Enter First String ")
    str2 = input("Enter Second String ")
    st1 = set(str1)
    # print(st1)
    st2 = set(str2)
    if st1 & st2:
        print(st1 & st2)
    else:
        print("No common Elements")


common_letters()
