num = 123
p=num
l = 0

while num != 0:
    digit = num % 10
    l = l * 10 + digit
    num = num // 10

print(l)

if(p==l):
    print("palindrome")

else:
    print("Not palindome")
 

