def length_last_words(A):
    arr = A.split(' ')
    print(arr)
    size = len(arr)
    if size == 1:
        return len(A)
    else:
        last_word = arr[-1]
        return (len(last_word))


print(length_last_words("Abin"))
