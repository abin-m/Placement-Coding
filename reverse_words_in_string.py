def reverse(str_r):
    str_r = str_r[::-1]
    return str_r


def reverse_words(str_r):
    n = len(str_r)
    if (n == 1):
        return str_r
    str2 = str_r.split(" ")
    size = len(str2)
    rev_all = ""
    for i in range(size):
        rev = reverse(str2[i])
        rev_all = rev_all+rev+" "
    d = reverse(rev_all)
    return (d.strip())


str = "Why you are not getting any jobs"
print(reverse_words(str))
