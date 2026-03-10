 # print("Enter two numebr:")
# n1,n2=map(int,input().split())

# max_num=max(n1,n2)
# print(max_num)

# i=max_num
    
# if(n1%i==0 and n2%i==0):
#         print(i)
#         i+=1


# for i in range(1,3):
#     for j in range(1,4):
#        print(f"i={i},j={j}")

# n=4
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()   

# n=4
# t=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print(t,end=" ")
#         t=t+1
#     print()   

# n=4
# t=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print(t,end=" ")
#         t=t+1
#     print()   


# n=4
# t=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print(chr(t),end=" ")
#         t=t+1
#     print() 
# 
# 

# 88877
# n=4
# t=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print(chr(t),end=" ")
#         t=t+1
#     print() 
 

# n=4
 
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print((i+j+1)%2,end=" ")

#     print() 



# n=4 
# for i in range(1,n+1):
#     for j in range(1,i+1):
        
#         print((i+j)%2,end=" ")

#     print() 

# n=3
# for i in range (n,0,-1):
#     for j in range (1,i+1):
#         print(j,end="\t")
#     print()

# n=3
# for i in range (n,0,-1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

n=3
for i in range (1,n+1):
    for k in range (n-1):
        print(" ",end=" ")
for j in range (1,i+1):
    print("*",end=" ")
print()