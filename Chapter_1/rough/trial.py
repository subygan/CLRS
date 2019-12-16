
arr = [5,4,3,6,1,2,2]

for i in range(1,len(arr)):

    value = arr[i]

    j = i-1
    while j>=0 and value<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = value

print(arr)
