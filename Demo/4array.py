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

def rotate(arr,k):
    n=len(arr)
    temp=arr[:k]
    for i in range(k,n):
        arr[i-k]=arr[i]

    for i in range(k):
        arr[n-k+i]=temp[i]     

arr=[1,2,3,4,5]
rotate(arr,1)
print(arr)