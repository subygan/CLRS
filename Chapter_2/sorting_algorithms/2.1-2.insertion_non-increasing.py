def insertion_decreasing(arr):

    for i in range(1, len(arr)):
        print(i)
        j = i-1
        value = arr[i]
        while j >= 0 and arr[j] < value:
            # shifting right by one
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = value

    return arr


print(insertion_decreasing([1,2,34,5,4,3]))
