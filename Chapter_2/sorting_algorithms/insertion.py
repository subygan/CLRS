
arr = [1,23,1,42,4,2,132,9]


for i in range(1,len(arr)):
    j = i-1
    value = arr[i]
    # print(value)


    while j>=0 and arr[j]>=value :

        print("while")
        #shifting right by one
        arr[j+1] = arr[j]
        j-=1
        print(arr)

    #assigning in the found spot
    arr[j+1] = value

