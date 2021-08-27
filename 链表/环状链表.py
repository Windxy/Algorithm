class ListNode():
    def __init__(self,x):
        self.data = x
        self.next = None
#是否有环
def hasCycle(self , head:ListNode):
    # 哈希
    # dict = set()
    # while head:
    #     if head not in dict:
    #         dict.add(head)
    #         head = head.next
    #     else:
    #         return True
    # return False
    # 快慢指针
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


