# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        例如  1--2--3--4--5  k=3   3--4--5--1--2
        :param head:
        :param k:
        :return:
        '''
        # dummy_node = ListNode(0)
        # dummy_node.next = head
        temp = head
        len = 1
        while head.next:
            head = head.next
            len += 1
        k = k%len-1 #may wrong
        head.next = temp        #环形
        for i in range(len-k):
            temp = temp.next
        res = temp.next
        temp.next = None
        return res
