def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid        
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

arr=[1,2,3,4,5,6,7]
binary_search(arr,5)



 