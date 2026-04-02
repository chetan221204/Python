# def running_sum(arr):
#     n=len(arr)
    
#     for i in range(1,n):
#         arr[i]=arr[i]+arr[i-1]

#     return (arr)


# arr=[1,1,1]
# print(running_sum(arr))


def running_arr(arr):
    n=len(arr)
    for i in range(1,n):
        arr[i]=arr[i]+arr[i-1]
    return arr

arr=[1,1,1]
print(running_arr(arr))