# def Secondlag_element(arr):
#     n=len(arr)
#     largest_element=float('-inf')
#     Secondlag_element=float('-inf')
#     for i in range(n):
#         if(arr[i]>largest_element):
#             largest_element=arr[i]
    
#     # return largest_element
#     for i in range(n):
#         if(arr[i]>Secondlag_element and arr[i]!=largest_element):
#             Secondlag_element=arr[i]

#     return Secondlag_element

# arr=[12,423,54,64,2324,64]
# print(Secondlag_element(arr))

# def secondlargest(arr):
#     n=len(arr)
#     largest=float('-inf')
#     slargest=float('-inf')
#     for i in range(n):
#         if(arr[i]>largest):
#             slargest=largest
#             largest=arr[i]
#         elif(arr[i]<largest and arr[i]>slargest):
#             slargest=arr[i]
#     return slargest

# arr=[11,22,44,55,66,77,88,345]
# print(secondlargest(arr))


# arr=[1,1,1,1,2,2,3,3,4,4,5,6,6,6,6,3,3,3,2,1,1]
# result=[]
# seen=set()
# for num in arr:
#     if num not in seen:
#         seen.add(num)
#         result.append(num)
# print(result)


# def dublicate(arr):
#     i=0
#     n=len(arr)
#     for j in range(1,n):
#         if(arr[j]!=arr[i]):
#             arr[i+1]=arr[j]
#             i+=1
#     return arr[:i+1]

# arr=[1,1,1,1,2,2,2,3,3,4,4,5,5]
# print(dublicate(arr))


# arr=[1,3,0,3,0,0,3,5,0,0,7,8]
# i=0
# for j in range(len(arr)):
#     if(arr[j]!=0):
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
# print(arr)




# arr=[1,0,0,2,3,0,0,0,2,3,4,0]
# i=0
# for j in range(len(arr)):
#     if arr[j]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
# print(arr)



# def reverse(arr,start,end):
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start +=1
#         end -=1
# def rotate(arr,k):
#     n=len(arr)
#     k=k%n
#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)
#     reverse(arr,0,n-1)
#     return arr

# arr=[1,2,3,4,5]
# print(rotate(arr,1))



def removeOuterParentheses(s):
    
    result = ""  
    # Initialize nesting level counter
    level = 0     
    # Traverse the string
    for char in s:
        # If we encounter '(', increase the level 
        if char == '(':
            # If we're inside a primitive, add '(' to result
            if level > 0:
                result += char
            # Increase the nesting level for '('
            level += 1  
        elif char == ')':
            # Decrease the nesting level for ')'
            level -= 1  
            # If we're inside a primitive, add ')' to result
            if level > 0:
                result += char
    # Return the final result after removing the outer parentheses
    return result
# Example usage
s = "(()())(())"  
print(removeOuterParentheses(s)) 