# a=1
# while a<=5:
#     print(a)
#     a+=1
    
# -------
# a=123
# count=0

# while a%10!=0:
#     l=a%10
#     count+=1
#     a=a//10
# print(count)

a=123
s=0

while a%10!=0:
    r=a%10
    s= s * 10 + r
    a=a//10
print(s)
