print(1)
print("Check matrix is square matrix or not")
lst = [[1,2,3],[4,5,6],[7,8,9]]
print(lst)
rows = len(lst)
is_square= True
for i in lst:
    if rows!=len(i):
        is_square= False
print(is_square)
"""
1
Check matrix is square matrix or not
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
True
"""
print("------------------------------------------------------------")
print(2)
print("diagonal elements.")
matrix = [[1,2],[3,4]]
res=[]
for i in range(len(matrix)): # 0 1 
    for j in range(len(matrix[i])): # 0 1 
        if i==j:
            print(matrix[i][j])
            res.append(matrix[i][j])
print(res)
"""
2
diagonal elements.
1
4
[1, 4]
"""
print("------------------------------------------------------------")
print(3)
print("Anti Diagonal elements.")
matrix = [[1,2],[3,4]]
res=[]
for i in range(len(matrix)): # 0 1 
    for j in range(len(matrix[i])): # 0 1 
        if i!=j:
            print(matrix[i][j])
            res.append(matrix[i][j])
print(res)
"""
3
Anti Diagonal elements.
2
3
[2, 3]
"""
print("------------------------------------------------------------")
print(4)
print("Non diagonal elements.")
matrix = [[1,2],
          [3,4]]
res=[]
for i in range(len(matrix)): # 0 1 
    for j in range(len(matrix[i])): # 0 1 
        if i!=j:
            res.append(matrix[i][j])
print(res)
"""
4
Non diagonal elements.
[2, 3]
"""
print("----------------------------------------------------------")
print(5)
print("Non-Anti Diagonal elements")
matrix = [[1,2],[3,4]]
res= []
n = len(matrix)
for i in range(n):
    for j in range(n):
        if i+j!=n-1:
            res.append(matrix[i][j])
print(res)
"""
5
Non-Anti Diagonal elements
[1, 4]
"""
print("----------------------------------------------------------")
print(6)
print("Lower Triangle Of matrix")
matrix = [[1,2],[3,4]]
n = len(matrix)
res=[]
for i in range(n):
    row=[]
    for j in range(n):
        if i>=j:
            row.append(matrix[i][j])
        else:
            row.append(0)
    res.append(row)
print(res)
"""
6
Lower Triangle Of matrix
[[1, 0], [3, 4]]
"""  
print("----------------------------------------------------------")
print(7)
print("Upper Triagle of matrix")
matrix = [[1,2],[3,4]]
n = len(matrix)
res=[]
for i in range(n):
    row=[]
    for j in range(n):
        if i<=j:
            row.append(matrix[i][j])
        else:
            row.append(0)
    res.append(row)
print(res)
"""
7
Upper Triagle of matrix
[[1, 2], [0, 4]]
"""
print("----------------------------------------------------------")
print(8)
print("Transpose of matrix")
matrix = [[1,2],[3,4]]
n = len(matrix)
res=[]
for i in range(n):
    row=[]
    for j in  range(n):
        row.append(matrix[j][i])
    res.append(row)
print(res)
"""
8
Transpose of matrix
[[1, 3], [2, 4]]
"""
print("----------------------------------------------------------")
print(9)
print("Check if Diagonal elements are same")
matrix = [[5,0],[0,5]]
n = len(matrix)
same = True
first = matrix[0][0]
for i in range(n):
    if matrix[i][i]!=first:
        same=False
        break
print(same)
"""
9
Check if Diagonal elements are same
True
"""
print("----------------------------------------------------------")
print(10)
print("Check if anti diagonal elements are same")
matrix = [[0,3],[3,0]]
n  = len(matrix)
first = matrix[0][n-1]
same = True
for i in range(n):
    if matrix[i][n-1-i] !=first:
        same = False
        break
print(same)
"""
10
Check if anti diagonal elements are same
True
"""
print("----------------------------------------------------------")
print(11)
print("Convert Diagonal Elements to zero")
matrix=[[1,2],[3,4]]
n = len(matrix)

for i in range(n):
    matrix[i][i]=0
print(matrix)
"""
11
Convert Diagonal Elements to zero
[[0, 2], [3, 0]]
"""
print("----------------------------------------------------------")
print(12)
print("convert anti diagonal elements to zero")
matrix = [[1,2],[3,4]]
n = len(matrix)
for i in range(n):
    matrix[i][n-1-i]=0
print(matrix)
"""
12
convert anti diagonal elements to zero
[[1, 0], [0, 4]]
"""
print("----------------------------------------------------------")
print(13)
print("convert Non diagonal elements to zero")

matrix = [[1,2],[3,4]]
n=len(matrix)

for i in range(n):
    for j in range(n):
        if i!=j:
            matrix[i][j]=0
print(matrix)
"""
13
convert Non diagonal elements to zero
[[1, 0], [0, 4]]
"""
print("----------------------------------------------------------")
print(14)
print("Sum of All Elements in matrix")
matrix = [[1,2],[3,4]]
total=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total+=matrix[i][j]
print(total)
"""
14
Sum of All Elements in matrix
10
"""
print("----------------------------------------------------------")
print(15)
print("Matrix multiplication")
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
row_a = len(a)
col_a = len(a[0])
col_b = len(b[0])
res=[]
for i in range(row_a):
    row=[]
    for j in range(col_b):
        total=0
        for k in range(col_a):
            total+= a[i][k]*b[k][j]
        row.append(total)
    res.append(row)
print(res)
"""
15
Matrix multiplication
[[19, 22], [43, 50]]

"""
