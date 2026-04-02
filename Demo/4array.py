# arr=[10,20,30,40,50]
# first=arr[0]
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]

# arr[len(arr)-1] = first 
# print(arr)

# ---Q2--
# def rotate(arr,k):
#     n=len(arr)
#     for _ in range(k):
#         first=arr[0]
#         for i in range(n-1):
#             arr[i]=arr[i+1]
        
#         arr[n-1]=first

# arr=[1,2,3,4,5]
# rotate(arr, 2)
# print(arr)


# # --Q3--

# def rotate(arr,k):
#     n=len(arr)
     
#     temp=arr[:k]
#     for i in range(k,n):
#         arr[i-k]=arr[i]
    
#     for i in range (k):
#         arr[n-k+i]=temp[i]

# arr=[10,20,30,40,50]
# rotate(arr,2)
# print(arr)

# --Q4--

# def reverse(arr, start, end): 
 
#     while start < end: 
#         arr[start], arr[end] = arr[end], arr[start] 
#         start += 1 
#         end -= 1  

# def rotate(arr, k): 
 
#     n = len(arr) 
 
#     reverse(arr,0,k-1) 
#     reverse(arr,k,n-1) 
#     reverse(arr,0,n-1) 
  
# arr = [1,2,3,4,5,6,7] 
# rotate(arr,2) 
# print(arr) 

 
# --Q5- Right_Rotation-

# def reverse(arr,start,end): 
 
#     while start < end: 
#         arr[start],arr[end] = arr[end],arr[start] 
#         start += 1 
#         end -= 1 
 
# def rotate_right(arr,k): 
#     n = len(arr) 
 
#     reverse(arr,0,n-1) 
#     reverse(arr,0,k-1) 
#     reverse(arr,k,n-1) 
 
# arr = [1,2,3,4,5] 
 
# rotate_right(arr,2) 
 
# print(arr)



# # --Q6-- Check if Two Arrays are Rotation
# # Hint: A+A contains B

# def is_rotation(A, B):
#     if len(A) != len(B):
#         return False
        
#     temp = A + A
#     n = len(temp)
#     m = len(B)
    
#     for i in range(n - m + 1):
#         if temp[i:i+m] == B:
#             return True
            
#     return False

# A = [1, 2, 3, 4, 5]
# B = [3, 4, 5, 1, 2]

# print(is_rotation(A, B))



# --Q7--
# string rotation

# def rotate(arr,k):
#     n=len(arr)
#     for _ in range(k):
#         first=arr[0]
#         for i in range(n-1):
#             arr[i]=arr[i+1]
        
#         arr[n-1]=first

# arr=list("abcdef")
# rotate(arr, 2)
# # print(arr)
# print("".join(arr))



# # --Q9-- Rotate First Row of Matrix
# def findMin(arr):
#         low, high = 0, len(arr) - 1

#         while low < high:
#             mid = (low + high) // 2

#             if arr[mid] > arr[high]:
#                 low = mid + 1
#             else:
#                 high = mid

#         return arr[low]

# arr=[2,3,4,5,6,1]
# print(findMin(arr))








# --Q10--
#Binary Search

# def BinarySearch(arr,target):
    
#     n=len(arr)
#     low=0
#     high=n-1
#     while low <=high:
#         mid= (low +high) //2

#         if (arr[mid] ==target):
#             return mid  

#         elif(arr[mid] >target ):
#             high=mid -1
#         else:
#             low=mid +1
#     return -1

# arr=[10,20,30,40,50]
# print(BinarySearch(arr,50))  



# #  Q11
# def search(arr, target):
#     lo, hi = 0, len(arr) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2

#         if arr[mid] == target:
#             return mid

#         # Left half is sorted
#         if arr[lo] <= arr[mid]:
#             if arr[lo] <= target < arr[mid]:
#                 hi = mid - 1    
#             else:
#                 lo = mid + 1    

#         else:
#             if arr[mid] < target <= arr[hi]:
#                 lo = mid + 1     
#             else:
#                 hi = mid - 1     

#     return -1   

# # Result
# print(search([2,3,4,5,6,7,1], 7))

Notice=["Do","follow", "Suryansh"]
for Notice in Notice:
    print(Notice)