# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 数塔
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/7 21:43
**************************************************
'''
'''http://acm.hdu.edu.cn/showproblem.php?pid=2084'''
'''
# 从顶层走到底层，求最大的数字之和
# 最优子结构max
# 输入数据首先包括一个整数C，表示测试实例的个数，每个测试实例的第一行是一个整数N(1 <= N <= 100)，表示数塔的高度，
# 接下来用N行数字表示数塔，其中第i行有个i个整数，且所有的整数均在区间[0,99]内。'''

l = []

C = int(input())    # 输入实例数

for i in range(C):
    temp = []
    N = int(input())    # 输入塔层数
    ans = [[] for i in range(N)]
    for k in range(N):
        temp.append(list(map(int,input().split(' '))))  # 数据输入
    for j in range(N):
        ans[N-1].append(temp[N-1][j])      # 边界输入
    for ii in range(N-2,0,-1):
        for jj in range(0,ii+1):
            ans[ii].append(max(ans[ii+1][jj],ans[ii+1][jj+1])+temp[ii][jj])     # 最优子结构状态转移方程
    print(temp[0][0]+max(ans[1][0],ans[1][1]))      # 输出结果