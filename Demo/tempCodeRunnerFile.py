(arr, start, end): 
 
    while start < end: 
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1 
        end -= 1  

def rotate(arr, k): 
 
    n = len(arr) 
 
    reverse(arr,0,k-1) 
    reverse(arr,k,n-1) 
    reverse(arr,0,n-1) 
  
arr = [1,2,3,4,5,6,7] 
rotate(arr,2) 
print(arr) 