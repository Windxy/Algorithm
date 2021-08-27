# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 二叉树的层平均值
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/12 20:41
**************************************************
'''
'''给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

from typing import List
from collections import deque       # 双端队列
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 层序遍历，获取节点，入队列，获取队列长度，求值加入
        q = deque()
        q.append(root)  # 初始化
        ans = [];ans.append(root.val)    # 初始化
        size = 1
        sum = 0
        while q:#一直到为空，没有节点了
            for i in range(size):
                tmp = q.pop()       # 出节点，获取节点

                left = tmp.left     # 获取左节点
                if left:
                    q.append(left)
                    sum+=left.val

                right = tmp.right   # 获取右节点
                if right:
                    q.append(right)
                    sum+=right.val
            size = len(q)
            if size!=0:
                ans.append(sum/size)
            sum = 0  # 初始化
        return ans
                # 获取长度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 题目数组非空，
        # if not root:
        #     return []

        # 返回结果
        res = []

        from collections import deque
        # 定义队列
        queue = deque()
        # 将根节点入队
        queue.append(root)
        # 队列不为空，表达式二叉树还有节点，循环遍历
        while queue:
            # 先标记每层的节点数
            size = len(queue)
            # 定义变量，记录每次节点值
            total = 0
            # 这里开始遍历当前层的节点
            for _ in range(size):
                # 出队
                node = queue.popleft()
                # 先将当前节点的值存储
                total += node.val
                # 节点的左右节点非空时，入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 添加每层的节点值均值
            res.append(total/size)
        return res
