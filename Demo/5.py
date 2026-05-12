# a=input()
# if(a==0):
#     print("0")
# elif(a==1):
#     print("$2000")
# elif(a==2 or a==3 ):
#     print("$5000")
# elif(a>=4 or a<=6):
#     print("$9000")
# elif(a==9):
#     print("12000")
# elif(a==12):
#     print("$15000")

# else:
#     print("error")


# def validate_transaction(n,transaction):
#     seen=set()
#     prev_time=None
#     for t in transaction:
#         sender,receiver,time,amount=t
#         time=int(time)

#         # check dublicate
#         if(sender,receiver) in seen:
#             return "ERROR DUPLICATION TRANSACTION"
#         seen.add((sender,receiver))

#         # Rule 2 : Time difference check
#         if prev_time is not None and (time - prev_time) >60:
#             return "FRAUD DETECTED"
#         prev_time= time
#     return "All TRANSACTION ARE VALID"

# n=3
# # n=int(input())
# # transaction=[]
# # for _ in range(n):
# #     data = input().split()
# #     transaction.append((data[0],data[1],data[2],data[3]))
# # result = validate_transaction(n,transaction)
# # print(result)
# transaction = [
#     # ("A","B",100,500),
#     # ("C","D",120,300),
#     # ("E", "F",350,200),
#      ("A","B",100,500),
#     ("C","D",120,300),
#     ("E", "F",250,200),
# ]
# print(validate_transaction(n,transaction))   



# is subString is  a part of a original string in the same order if yes print positive or negative
# def is_subsequence(a,b):
#     i = 0
#     j = 0

#     while i<len(a) and j<len(b):
#         if(a[i]==b[j]):
#             j+=1
#         i+=1
#     return j==len(b)

# a=input().strip()
# n= int(input())
# for _ in range(n):
#     b= input().strip()
#     if is_subsequence(a,b):
#         print("POSITIVE")
#     else:
#         print("NEGATIVE")         
# # a='coronavirus'
# # b='virus'


 
# def trafficSignal(timer):
#     if(timer==0):
#         return "Green"
#     elif(timer==30):
#         return "Orange"
#     elif(30 <timer <=90):
#         return "Red"
#     else:
#         return "Invalid"
    
# timer=int(input())
# trafficSignal(timer)



def countDigitOccurrences(arr, digit):
    count=0
    for i in range(len(arr)):
        num=arr[i]
        while  num!=0:
            if(num%10==digit):      
                count=count + 1
            num//=10
    return count

arr=[12,54,32,22]
digit=2
print(countDigitOccurrences(arr,digit))