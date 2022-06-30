def solve(n,arr,key):
    left , right = 0 , n
    while left < right:
        mid = left + (right-left)//2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

#Has to be sorted
# arr = [1,3,4,5,10]
arr = [1,2,3,4,4,4,5,5,5,6,6,7,7,7,7,8,9,10,11,12,13,14]
print(solve(len(arr),arr,4))
