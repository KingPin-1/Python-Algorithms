
def insertionSort(arr):
    n = len(arr)
    for wall in range(n):
        curr = arr[wall]
        i = wall-1
        while i >= 0 and curr < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = curr

temp = [12,9,14,7,3,1,5,6,8]
print(temp)
insertionSort(temp)
print(temp)