def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)

def merge(arr,left,right):
    i = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1
    
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1

temp = [12,9,14,7,3,1,5,6,8,2]
print(temp)
mergeSort(temp)
print(temp)