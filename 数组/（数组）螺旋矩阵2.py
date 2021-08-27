# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）螺旋矩阵2
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/21 9:19
**************************************************
'''
'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化
        ans = [[0 for i in range(n)] for i in range(n)] #不能用[[0]*n]*n
        dx = [0, 1, 0, -1]  # 方向：右，下，左，上
        dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
        di = 0  # 初始化方向变量
        visited = [[0 for i in range(n)] for i in range(n)]
        x,y = 0,0

        for i in range(n*n):
            ans[x][y]=i+1
            visited[x][y]=1
            if not(0<=x + dx[di]<n and 0<=y + dy[di]<n) or visited[x + dx[di]][y + dy[di]]:#如果超过了，或者访问过了
                di=(di+1)%4
            x = x + dx[di]
            y = y + dy[di]
        return ans
s = Solution()
s.generateMatrix(4)