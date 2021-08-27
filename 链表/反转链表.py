# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ReverseList(self, pHead:ListNode):
    cur = pHead
    pre = None
    nex = None
    # 画个图看看
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return cur
