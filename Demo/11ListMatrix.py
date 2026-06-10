# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # for row in matrix:
# #     print(row)

# # print(matrix)
# matrix[1][1]=11
# print(matrix)

# ------x------x-----

# matrix=[]
# row,col=3,3
# for _ in range(row):
#     matrix.append([0]*col)

# print(matrix)



# Transposse of a matrix 
# list=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3): 
#         print(list[j][i],end=" ")
#     print()



# Adddition of two matrix

# list1=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print("Matrix-1")
# for i in range(3):
#     for j in range(3): 
#         print(list1[j][i],end=" ")
#     print()

# list2=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print("Matrix-2")
# for i in range(3):
#     for j in range(3): 
#         print(list2[i][j],end=" ")
#     print() 

# list3=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# print("Adddition of two matrix:")
# for i in range(3):
#     for j in range(3): 
#         list3[i][j]=list1[i][j]+list2[i][j]

# for i in range(3):
#     for j in range(3): 
#         print(list3[i][j],end=" ")
#     print() 




# lower triangle
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         if i>=j:
#             print(matrix[i][j],end=" ")
#     print()


# Upper-Triangle
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         if i<=j:
#             print(matrix[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# Diagonal Matrix
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print(matrix[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# Reverse Diagonal Matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n=len(matrix)
for i in range(3):
    for j in range(3):
        if (i+j==n-1):
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
