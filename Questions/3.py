# # Bulb swiching problem  using square root 
# n=int (input())
# for i in range(1,n+1):
#     root=int (i**0.5)

#     if root*root == i:
#         print("ON",end=" ")
#     else:
#         print("OFF",end=" ")



# bubble sort
# lib  
# fuction tool 
# collection 
# pemutation 
# combination

# a4k3b2
# aeknbd

# def character(a):
# #     a
# print(chr(65))
# print(ord("a"))



# a=123
# while a%10!=0:
#     x=a%10
#     z=x*10+x
#     a=a/10
#     print(z)

# n='ideal software solution'
# a=n.split(" ")
# print(a)
# n1=len(a)
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=" ")






def reveres(world1,start,end):
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1


world1=str(input())
world2=str(input())
reveres(world1,0)