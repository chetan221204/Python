# d1={}
# d1[1]='apple'
# d1[2]='mango'
# print(d1)    

# rec={}
# n=int(input("Enter number of Student:"))
# i=1
# while i<=n:
#     name=input("Enter Student Name:")
#     marks=input("Enter % of marks of student: ")
#     rec[name]=marks
#     i=i+1
# print("Name of Student","\t","% of marks")
# for i in rec:
#     print("\t",i,"\t\t",rec[i])



# a=10
# b=20
# print("a=",a)
# print("b=",b)
# # a=a+b
# # b=a-b
# # a=a-b
# c=b
# b=a
# a=c
# print("a=",a)
# print("b=",b)


# Bubble Sort

arr=[]
n=int(input("Enter SIZE:"))
print("Enter Elements:")
for i in range(n):
    num=int(input())
    arr.append(num)


for i in range(n-1):
    swapped=False
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break

print("Sorted Array:",arr)