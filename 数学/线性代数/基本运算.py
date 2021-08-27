# import numpy as np
from sympy import *
D = Matrix(             # 度矩阵
    [[1,0,0,0],
     [0,3,0,0],
     [0,0,2,0],
     [0,0,0,2]]
)
A = Matrix(             # 邻接矩阵
    [[0,1,0,0],
     [1,0,1,1],
     [0,1,0,1],
     [0,1,1,0]]
)
H0 = Matrix([
    [0, 0],
    [1, 1],
    [2, -1],
    [-3, 4]],
    dtype=float
)
C = D**(-1)
# A_new = A+eye(4)
New_H = C*A*H0
for i in range(10):
    New_H = C*A*New_H
print(New_H)

# I = eye(4)
# C = D**(-1/2)
# # print(C)
# L = D-A
# print(C*L)
# # print(I-C*A*C)