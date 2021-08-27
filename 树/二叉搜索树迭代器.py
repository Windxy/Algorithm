# https://leetcode-cn.com/problems/binary-search-tree-iterator/
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0

if __name__ == '__main__':
    queue = collections.deque()
