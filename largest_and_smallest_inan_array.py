def maximum(arr):
    max = arr[0]
    size = len(arr)

    for i in range(size):
        if (arr[i] > max):
            max = arr[i]
    return max


arr = [63, 54, 98, 34, 89, 42, 18]
print("Maximum value from the array:", maximum(arr))


def minimum(arr):
    min = arr[0]
    size = len(arr)

    for i in range(size):
        if (arr[i] < min):
            min = arr[i]
    return min


print("Minimum value from the array:", minimum(arr))
