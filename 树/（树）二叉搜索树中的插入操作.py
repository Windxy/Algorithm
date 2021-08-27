# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）二叉搜索树中的插入操作
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/30 9:08
**************************************************
'''
'''
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 
输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
例如, 
给定二叉搜索树:
        4
       / \
      2   7
     / \
    1   3
和 插入的值: 5
你可以返回这个二叉搜索树:
         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:return TreeNode(val,None,None)
        def helper(root):
            if root.val > val and root.left:
                helper(root.left)
            if root.val < val and root.right:
                helper(root.right)
            if root.val > val and root.left is None:
                root.left = TreeNode(val,None,None)
            if root.val < val and root.right is None:
                root.right = TreeNode(val,None,None)
            return
        helper(root)
        return root