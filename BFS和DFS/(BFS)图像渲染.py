# https://leetcode-cn.com/problems/flood-fill/
from typing import List
import collections
'''有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
最后返回经过上色渲染后的图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flood-fill
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 连通区域全变为newColor
        # 方法1，BFS，用queue
        queue = collections.deque()
        # append 和 popleft方法

        Rows = len(image)
        Cols = len(image[0])
        # 初始化
        turnLRTD = [[-1,0],[1,0],[0,1],[0,-1]]
        oldColor = image[sr][sc]
        queue.append((sr,sc))
        while queue:
            nowX,nowY = queue.popleft() # 当前的行和列
            # 上下左右遍历
            for a,b in turnLRTD:
                if nowX+a < Rows \
                and nowX+a >= 0 \
                and nowY+b < Cols \
                and nowY+b >= 0 \
                and image[nowX+a][nowY+b]==oldColor:
                    queue.append((nowX+a,nowY+b))
                    image[nowX+a][nowY+b] = newColor
        return image

        # 方法2 DFS
        # oldColor = image[sr][sc]
        # Rows = len(image)
        # Cols = len(image[0])
        #
        # def helper(x,y):
        #     if image[x][y] == oldColor:
        #         image[x][y] = newColor
        #         for a,b in turnLRTD:
        #             if x+a < Rows \
        #             and x+a >= 0 \
        #             and y+b < Cols \
        #             and y+b >= 0 \
        #             and image[x+a][y+b]==oldColor:  # 提前剪枝
        #                 helper(x+a,y+b)
        #
        # if oldColor == newColor:
        #     return image
        # helper(sr,sc)
        # return image