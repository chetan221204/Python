# removing the vowel and the showing is without it 
# def func(h):
#     vowels="AEIOUaeiou"
#     result=''
#     for ch in h:
#         if ch not in h:
#             result+=ch
#     return 

# def main():
#     h=str(input())
#     result=func(h)
#     print(result)

# if __name__=="__main__":
#     main()


# def func(h):
#     vowels="AEIOUaeiou"
#     result=''
#     for ch in h:
#         if ch not in vowels:
#             result+=ch
#     return result

# def main():
#     h =input()
#     result = func(h)
#     print(result)

# if __name__=="__main__":
#     main()

# Q2
# 25 77 54 81 48 34
# import math 
# def countCoustomer(bills):
#     count=0
#     for b in bills:
#         root=int(math.sqrt(b))

#         if root*root==b:
#             count+=1
#     return count
        
# def main():
#     n=int(input())
#     bills=list(map(int,input().split()))
#     result=countCoustomer(bills)
#     print(result)

# if __name__=="__main__":
#     main()


# 3

# def checkAdsCode(arr,n,k):
#     for i in range(0,n,3):
#         group=arr[i:i+3]
#         if k not in group:
#             return 0
#     return 1
          

# def main():
#     n=int(input()) #6
#     arr=list(map(int,input().split())) #101 102 101 203 101 502
#     k=int(input())
#     result=checkAdsCode(arr,n,k)
#     print(result)


# def checkAdsCode(arr, n, k):
#     for i in range(0, n, 3):
#         group = arr[i:i+3]

#         if k not in group:
#             return 0

#     return 1


# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     k = int(input())

#     result = checkAdsCode(arr, n, k)
#     print(result)

# if __name__=="__main__":
#     main()

# 4
# def evenfrequency(s): #aaabbacccdd
#     n=len(s)
#     total=0
#     count=1
#     for i in range(1,n):
#         if s[i] ==s[i-1]:
#             coint+=1

# def evenfrequency(s):   # aaabbacccdd
#     n = len(s)
#     count = 1
#     total = 0

#     for i in range(1, n):

#         if s[i] == s[i - 1]:
#             count += 1

#         else:
#             if count % 2 == 0:
#                 total += count
#             else:
#                 total += count - 1

#             count = 1

#     # last group
#     if count % 2 == 0:
#         total += count
#     else:
#         total += count - 1

#     print(total)


# evenfrequency("aaabbacccdd")


# prices =[100,60,70,65,80,85]
# n=len(prices)
# for i in range(n):
#     span=1
#     j=i-1
#     while j>=0 and prices[j]<=prices[i]:
#         span+=1
#         j-=1
#     print(span,end=' ')



# arr=[1,2,3,4,5]
# for i in range(len(arr)-1,0,-1):
#     print(i)
# def count(arr,n):
#     result = [0]*n
#     for i in range(n):
#         steps=arr[i]
#         for j in range(1,steps+1):
#             if i-j>0:
#                 result[i-j]+=1
#     return result

# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result=count(arr,n)
#     print(result)


# if __name__=="__main__":
#     main()



# a = 'abacba'

# s = set()

# for i in range(len(a)):
#     if a[i] not in s:
#         s.add(a[i])

# print(s)
 


 