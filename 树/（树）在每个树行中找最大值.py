# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
'''

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.ans = []
        # 层序遍历
        Q = deque()
        Q.append(root)

        while Q:
            N = len(Q)
            tmp = Q[0].val

            for i in range(N):
                tmp_node = Q.popleft()
                tmp = max(tmp, tmp_node.val)
                if tmp_node.left: Q.append(tmp_node.left)
                if tmp_node.right: Q.append(tmp_node.right)

            self.ans.append(tmp)
        return self.ans


