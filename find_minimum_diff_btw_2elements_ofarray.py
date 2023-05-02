

# algo

# 1:Sort the array
# 2:Initialise the first difference value to the largest, start comparing the difference of first elements with it.
# 3:compare elements with its adjacent elemnt & keep track of minimum difference


def minimum_diff_ele(arr):
    arr = sorted(arr)
    size = len(arr)
    min_diff = 9999*999

    for i in range(size-1):
        if (arr[i+1]-arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
    return min_diff


arr = [5, 32, 45, 4, 12, 18, 25]
print("The minimu difference between elements of an array is", minimum_diff_ele(arr))
