# print("Hello Chetan")

#   concatenation
#  print("Hello" + " World")

# str="Chetan"
# print(len(str))

# str="Chetan_Chauhan"
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])
# print(str[5])
# print(str[6])
    
# Slicing
# str="Chetan_Chauhan"
# print(str[0:6])
# print(str[7:14])

# str="APPLE"
# print(str[-5:-1])

# str="i am a coder" 
# print(str.endswith("er"))
# print(str.capitalize())
# print(str.find("coder"))
# print(str.count("a"))
# print(str.replace("coder","singer"))  

# a=20
# b=20
# if(a<b):
#     print("Hello")
# elif(a>b):
#     print("bye")
# else:
#     print("nikalo")

# Grade System
# a=int(input("Enter a Num:"))
# if(90<a<100):
#     print("A")
# elif(80<a<90):
#     print("B")
# elif(70<a<80):
#     print("C")
# elif(a<70):
#     print("D")
# else:
#print("Invalid Input")  

    
# a=int(input("Enter a Number:"))
# if(a%2==0):
#     print("Number is even")
# else:
#     print("Nuumber is odd")

# print(10//3)
# print(2**3**2)
# print(5==5.0) 
# print(5>3>1)
# print(True and False) **
# print(True or False)
# print(2**3**2)

# n=125
# l=0
# while n!=0:
#     n=n//10
#     l+=1

# print(l)


# username= input("Enter the Username:")
# password=input("Enter the password:")

# if(username=="admin" and password=="1234"):
#     print("Login Scessfull")
# else:
#     print("invalid")


# a=input("Enter a:")
# b=input("Enter b:")
# c=input("Enter c:")


# if(a>b and a>c):
#     print("A is greater ")
# elif(b>a and b>c) :
#     print("b is greater")
# elif(c>a and c>b):
#     print(" C is greater")
# else:
#     print("a , b , c are equal ")


# a=123
# reverse=0

# while reverse !=0 :
#     remainder = a % 10
#     reverse= reverse*10+remainder
#     a = a // 10

# print(reverse)


# num = 125
# p=num
# l = 0

# while num != 0:
#     digit = num % 10
#     l = l * 10 + digit
#     num = num // 10
# # print(l)

# while l !=0:
#     reverse  = l % 10    
#     l=l//10
    
#     print(reverse)

# n = 224
# all_even=True

# while n != 0:
#     t =n%10

#     if t%2!=0:
#         all_even = False
#         break
#     n=n//10

# print(all_even)

# a=123
# Max=0

# while a!=0:
#     digit=a%10
    
#     if(digit>Max):
#         Max=digit
#     a=a//10
# print(Max) 
   
a=221322
t=2
count=0

while a!=0:
    digit=a%10

    if(t==digit):
        count=count+1
    a=a//10
print(count);        