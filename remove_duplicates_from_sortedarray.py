def remove_duplicate_space(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    temp = [0]*n
    pivot = 0
    for last_occur in range(0, n-1):
        if arr[last_occur] != arr[last_occur+1]:
            temp[pivot] = arr[last_occur]
            pivot = pivot+1
    temp[pivot] = arr[n-1]
    return temp[0:pivot+1]


arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_duplicate_space(arr))
print("With Set method", list(set(arr)))
