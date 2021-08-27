'''
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 假设共同长度为c，那么一定满足a + c + b = b + c + a
        # 因此，两个链表分别从头开始，如果到了结尾，就返回到另一条链表的头，从新出发，最终一定会到交点或NULL
        TempA = headA
        TempB = headB
        while TempA != TempB:
            TempA = TempA.next if TempA else headB
            TempB = TempB.next if TempB else headA
        return TempA