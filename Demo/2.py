# For Loop
 

#  # Question1
# Sum of n Number
# a=int(input("Enter the Number"))
# sum=0
# while a!=0:
#     x=a%10
#     sum=sum+x
#     a=a//10
# print(sum)



# for i in range (1,5):
#     print(i)



# # using for loop
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

# for i in range (3):
    # print(i)
# for i in range (1,4):
#     print(i)
# for i in range (1,10,2):
#     print(i)


# # Q1
# for i in range(1,11,1):
#     print(i)

# # Q2
# n=int(input("Enter a Number:"))
# for i in range(1,n+1,1):
#     print(i)

# # Q3
# for i in range(1,11,2):
#     print(i)

# # Q4
# for i in range(2,11,2):
#     print(i)

# # Q5
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     print(i)


# # # Q6
# n=4
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)


# # Q7
# n=7
# fact=1
# for i in range(1,11):
#     print("7","*",i,"=",i*n)
     

# # # Q8
# # Febonaacii
# a = 0
# b = 1
# n = int(input("Enter number: "))

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# # Q9
# for i in range(1,101):
#     if i>=20 and i<=30:
#         continue
    # print(i)


# # Q10 Prime Number
# a=12
# for i in range(2,a):
#     if a%i==0:
#         print("Not a Prime Number")
#         break
# else:
#     print("Prime Number")


# # LCM 
# print("Enter two numebr:")
# n1,n2=map(int,input().split())

# # max_num=max(n1,n2)
# for i in range (2,n1*n2+1):
#     if(i%n1==0 and i%n2==0):
#         print(i)
#         break



# # HCF
print("Enter Two Number:")
# count=020
x,y=map(int,input().split())
min_num=min(x,y)
for i in range(1,min_num+1):
    if(x%i==0 and y%i==0):
        # count+=1
        print(i)
# print("Count is",count)

