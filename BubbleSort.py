
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

temp = [12,9,14,7,3,1,5,6,8]
print(temp)
bubbleSort(temp)
print(temp)