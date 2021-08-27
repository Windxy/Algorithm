# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）螺旋矩阵
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/16 9:38
**************************************************
'''
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        x = y = 0  # 矩阵元素位置初始化
        res = []  # 初始化，存储遍历后的矩阵元素
        dx = [0, 1, 0, -1]  # 方向：右，下，左，上
        dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
        di = 0  # 初始化方向变量
        visited = set()  # 初始化集合，存储已走过的坐标
        m, n = len(matrix), len(matrix[0])  # 矩阵的行列

        for i in range(m * n):  #
            res.append(matrix[x][y])  # 存储遍历矩阵过的元素
            visited.add((x, y))  # 存储遍历过的坐标
            tx, ty = x + dx[di], y + dy[di]  # 先记录下一步坐标，用于判断下一步怎么走
            if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited:  # 判断坐标是否需变向，且没有遍历过
                x, y = tx, ty
            else:
                di = (di + 1) % 4  # 改变方向，右下左上为一圈，防止方向坐标越界
                x, y = x + dx[di], y + dy[di]  # 下一步坐标
        return res

# 作者：HUST_PDE_YCX
# 链接：https://leetcode-cn.com/problems/spiral-matrix/solution/yong-shi-40ms-xiao-hao-137mb-mei-bu-xiang-xi-zhu-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。