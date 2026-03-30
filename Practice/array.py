# arr=[10,20,30,40,50]
# first=arr[0]
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]
    
# arr[len(arr)-1] =first
# print(arr)


# def rotate(arr,k):
#     n=len(arr)

#     for _ in range(k):
#         first=arr[0]
#         for i in range(len(arr)-1):
#            arr[i]=arr[i+1]
        
#     arr[n-1] =first
# arr = [1,2,3,4,5]
# rotate(arr,2)
# print(arr)


# def rotate(arr,k):
#     n=len(arr)
#     temp=arr[:k]
#     for i in range(k,n):
#         arr[i-k]=arr[i]
#     for i in range(k):
#         arr[n-k+i]=temp[i]
# arr = [1,2,3,4,5]
# rotate(arr,2)
# print(arr)


# def reverse(arr,start,end):
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start += 1
#         end -= 1
    
# def rotate(arr,k):
#     n=len(arr)

#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)
#     reverse(arr,0,n-1)

# arr=[1,2,3,4,5,6,7]
# rotate(arr,2)
# print(arr)



# # right rotation
# def reverse(arr,start,end):
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start += 1
#         end -= 1
    
# def rotate(arr,k):
#     n=len(arr)

#     reverse(arr,0,n-1)
#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)

# arr=[1,2,3,4,5]
# rotate(arr,2)
# print(arr)



# 21-03-2026
# is array rotation
def isrotation(a,b):
    if(len(a)!=len(b)):
        return False
    
    temp=a+a

    for i in range (len(a)):
        if b==temp[i:i+len(b)]:
            return True
    return False

print(isrotation([1,2,3,4,5],[3,4,5,1,2]))


# x="abcdef"
# k=2
# print(x[2:])
# Q--2
# def rotate(s,k):
#     k=k%len(s)
#     return(s[k:]+s[:k])
# print(rotate("abcdef",2))




def rotate_row_right(matrix,row,k):
    n=len(matrix[row])
    k=k%n
    # print(matrix[row][:-k])
    matrix[row] = matrix[row][-k:]+matrix[row][:-k]
    return matrix

# def rotate_row_left(matrix,row,k):
#     n=len(matrix[row])
#     k=k%n
#     print(matrix[row][:k])
#     matrix[row] = matrix[row][k:]+matrix[row][:k]
#     return matrix

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
# print(matrix[1][1])

print(rotate_row_right(mat,0,1))
# print(rotate_row_left(mat,0,1))






# Q--4
# n=len(matrix[i])
# k=k%n
# def rotate_all_row(matrix,k):
#     for i in range(len(matrix)):
#         matrix[i] =  matrix[i][-k:]+matrix[i][:-k]
#         return matrix

# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# print(rotate_all_row(mat,1))


# Binary Search
# import bisect

# arr=[10,20,30,40,50,60]

# target=30
# # i=bisect.bisect_left(arr,target)
# i=bisect.bisect_right(arr,target)
# print(i)
# # print(i if i<len(arr) and arr[i]==target else -1)



# def BinarySearch(arr,target):
#     low=0
#     high=len(arr)-1

#     while low<=high:
#         mid =(low+high)//2
#         if arr[mid] ==target:
#             return mid
#         elif arr[mid]<target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# arr=[10,20,30,40,50,60]
 
# print(BinarySearch(arr,40))
# print(BinarySearch(arr,100)) 