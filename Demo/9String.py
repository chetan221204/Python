# s="chetan"
# print(s[::-1])


# s=input("Enter main String:")
# subs=input("Enter sub string:")
# flag=False
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(subs,pos+1,n)
#     if pos==-1:
#         break
#     print("found at position",pos)
#     flag=True
# if flag ==False:
#     print("NOt Found")


# s = "chetanchauhan"
# print(s.count("a",5,20))


# ls=s.split()
# for i in ls:
#     print(i)
# s="Chetan Chauhan isa Boy"
# # print("".join(reversed(s)))
# print(s[::-1])


# s=input("Enter the String:")
# x={'a','e','i','o','u','A','E','I','O','U'}
# for i in s:
#     if i not in x:
#         print(i,end="") 


# a="aaabbaccccdd"
# for i in a

# s="Learing Python is very easy!!"
# x=s.split()
# l1=[]
# i=len(x)-1
# while i>=0:
#     l1.append(x[i])
#     i-=1
# print(" ".join(l1)) 


# s=input()
# x=s.split()
# target = ""
# for i in x:
#     a=i[::-1]
#     target=target+" "+ a
# print(target)


# s1=input("Enter First Character:")
# s2=input("Enter Second Character:")
# i,j=0,0
# output=""
# while i<len(s1) or j<len(s2):
#     if i<(len(s1)):
#         output=output+s1[i]
#         i+=1
#     if j<(len(s2)):
#         output=output+s2[j]
#         j+=1
# print(output)



# a="B4A1D3"
# s1=""
# s2=""
# output=""
# for i in a:
#     if i.isalpha():
#         s1=s1+i
#     else:
#         s2=s2+i

# for i in sorted(s1):
#     output=output+i
# for i in sorted(s2):
#     output=output+i
# print(output)



# a="a4b3c2"
# output=""
# previous=""
# t=""
# for i in a:
#     if i.isalpha():
#         previous=i
#     else:
#         t=previous*int(i)
#         output=output+t

# print(output)


# a="a4k3b2"
# output=""
# previous=""
# t=""
# for i in a:
#     if i.isalpha():
#         previous=ord(i)
#         output=output+i
#     else:
#         t=previous+int(i)
#         output=output+(chr(t))
# print(output)




# import math 
# a=int(input())
# count=0
# bills= list(map(int,input().split()))
# for i in bills:
#     root=int(math.sqrt(i))
#     if (root*root)==i:
#         count+=1
# print(count)


