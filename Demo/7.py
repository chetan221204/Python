# from itertools import combinations
# # for combo in combinations("ABCD", 3): 
# #     print("".join(combo))
# nums = [1, 2, 3, 4] 
# for combo in combinations(nums, 2):
#     print(combo)



# from itertools import combinations
# for i in combinations([1,2,3,4], 3):
#     print("".join(i))
#     # print(i)


# from itertools import combinations
# nums = [1, 3, 7, 5, 9] 
# for combo in combinations(nums, 2): 
#     if sum(combo) == 10: 
#         print("Found:", combo) 



# import math
# print(math.comb(10,2))


# from itertools import combinations_with_replacement
# for combo in combinations_with_replacement([1,2,3],2):
#     print(combo)


# from itertools import combinations
# members = ['Sunny', 'sameer', 'amit', 'shivanshu'] 
# committees = list(combinations(members, 2)) 
# print(f"Total possible 2-member committees: {len(committees)}") 
# print(committees) 


# from itertools import combinations 
# numbers = range(1, 50) 
# lotto_combos = list(combinations(numbers, 6)) 
# # print("Total possible combinations:", len(lotto_combos))  # Over 13 million 
# print("Sample ticket:", lotto_combos[100])
  

#Combination 
# from itertools import permutations
# data =['A','B','C']
# for combo in permutations(data,2):
#     print("".join(combo))