#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        cur = head
        while cur is not None:
            while cur.next.val == cur.val and cur.next is not None:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre = cur.next

            cur = cur.next
        return dummy_node.next