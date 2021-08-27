import numpy as np

'''邻接矩阵'''
A = np.matrix([
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]],
    dtype=float
)
'''特征矩阵'''
H0 = np.matrix([
    [0, 0],
    [1, 1],
    [2, 1],
    [5, 3]],
    dtype=float
)
'''权重矩阵'''
W = np.matrix([
    [1, -1],
    [-1, 1]]
)
'''激活函数'''
def func_relu(X:np.matrix):
    X[X<0] = 0
    return X

'''方案1'''
layeri = func_relu(A*H0*W)
# for i in range(10):
#     layeri = func_relu(A*layeri*W)
H_out = layeri
print("方案1",H_out)

'''方案2'''
D = np.array(np.sum(A, axis=0))[0]  #  度矩阵
D = np.matrix(np.diag(D))           #  然后转换为对称矩阵
L = D - A                           #  拉普拉斯矩阵
layeri = func_relu(L*H0*W)
# for i in range(10):
#     layeri = func_relu(L*layeri*W)
H_out = layeri
print("方案2",H_out)

'''方案3'''
I = np.eye(A.shape[0])
I = np.matrix(I)                    # 单位矩阵
A = A + I
D = np.array(np.sum(A, axis=0))[0]  # 度矩阵
D = np.matrix(np.diag(D))           # 然后转换为对称矩阵
L = (np.sqrt(D**(-1))) * (A) * (np.sqrt(D**(-1)))       # 拉普拉斯矩阵
layeri = func_relu(L*H0*W)
# for i in range(10):
#     layeri = func_relu(L*layeri*W)
H1 = layeri
print("方案3",H1)
