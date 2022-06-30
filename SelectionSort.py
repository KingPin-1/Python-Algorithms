def selectSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx] , arr[i] = arr[i] , arr[min_idx]

temp = [12,9,14,7,3,1,5,6,8]
print(temp)
selectSort(temp)
print(temp)