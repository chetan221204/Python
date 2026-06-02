# n=int(input("Enter the number:"))
# even_sum=0
# odd_sum=0
# while n!=0:
#     x=n%10
#     if x%2==0:
#         even_sum+=x
#     else:
#         odd_sum+=x
#     n=n//10
# print(odd_sum)
# print(even_sum)
# print(odd_sum*even_sum)


# n=int(input("Enter a Number:"))
# sum=0
# while n!=0:
#     x=n%10
#     sum=sum*10+x 
#     n=n//10
# a=0
# while sum!=0:
#     y=sum%10
#     print(y)
#     sum=sum//10



# largest digit

# a=59283
# larg=0
# while a!=0:
#     x=a%10
#     if x>larg:
#         larg=x
#     a=a//10
# print(larg)



# a=2514795
# even=0
# odd=0
# while a!=0:
#     x=a%10
#     if(x%2==0):
#         even+=x
#     else:
#         odd+=x
#     a=a//10

# product=even*odd
# print(even)
# print(odd)
# print(product)

# a=121
# y=a
# u=0
# while a!=0:
#     x=a%10
#     u=u*10+x
#     a=a//10
    
#     if (y==u):
#         print("Its a palindrome ")


# # factprial
# n=int(input())
# fact=1
# for i in range(1,10+1):
#     fact=n*i
#     print(n,"*",i,"=",fact)


# n=int (input())
# a=0
# b=1
# print(" ",a," ",b,end="")
# for i in range(1,n):
#     c=a+b
#     print(" ",c,end="")
#     a=b
#     b=c

 
# Prime Number
# a=int(input())
# prime_number=True
# for i in range(2,a):
#     if (a%i==0):
#         prime_number=False
#         break
# if(prime_number==False):
#     print("It's Not a  Prime Number")
# else:
#     print("It's a Prime Number")



# LCM
n1,n2=map(int ,input().split())
max_num=max(n1,n2)
while True:
    if(max_num%n1==0 and max_num%n2==0):
        print("LCM Of",n1,"and",n2,"is",max_num)
        break

    max_num+=1