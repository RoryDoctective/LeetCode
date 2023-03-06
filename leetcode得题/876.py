# 链表得head是有数值的


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一 自己写的
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count length
        b = head
        count = 1
        while b.next != None:
            count += 1
            b = b.next

        # half it
        half = int(count / 2) + 1

        # get it
        b = head

        for i in range(half - 1):
            b = b.next
        return b

# 二 快慢指针
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针
        fast = head
        slow = head

        while True:
            fast = fast.next
            if fast == None:
                return slow

            fast = fast.next
            slow = slow.next
            if fast == None:
                return slow
