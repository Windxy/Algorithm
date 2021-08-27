# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）求根到叶子节点数字之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/29 14:49
**************************************************
'''
'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
示例 1:
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''深度优先遍历'''
        def helper(root,temp):
            if root == None:
                return 0
            temp = root.val + temp*10
            if root.left == None and root.right==None:  #达到叶子节点了！
                return temp
            a = helper(root.left,temp)   # 左遍历
            b = helper(root.right,temp)  # 右遍历
            return a+b
        ans = helper(root,0)
        return ans