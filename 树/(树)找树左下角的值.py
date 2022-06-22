'''
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。
https://leetcode.cn/problems/find-bottom-left-tree-value/
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        # 层序遍历，找到最后一层
        De = deque()
        De.append(root)
        ans = 0
        while len(De):
            N = len(De) # 当前层有N个节点
            ans = De[0].val
            for i in range(N):
                now_node = De.popleft()
                if now_node.left:
                    De.append(now_node.left)
                if now_node.right:
                    De.append(now_node.right)
        return ans