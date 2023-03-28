'''
链表， swap nodes
方法：
    1. 双指针
    2. 递归/迭代

'''

# 递归化简单版
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base
        if not head or not head.next:
            return head
        # swap
        newHead = head.next
        head.next = self.swapPairs(head.next.next)
        newHead.next = head
        return newHead


# 递归
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base
        if head is None:
            return None
        if head.next is None:
            return head

        # setting
        p1= dummy = ListNode(-1,head)
        p2 = head

        # swap
        p1.next = p1.next.next
        p2.next = self.swapPairs(p2.next.next)
        p1.next.next = p2
        return dummy.next



# 自己写的双指针+稍微化简
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1= dummy = ListNode(-1,head)
        p2 = head

        while p2 is not None and p2.next is not None:
            # swap
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1.next.next = p2
            # update
            p1 = p1.next.next
            p2 = p2.next
        return dummy.next


# 自己写的双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1= dummy = ListNode(-1,head)
        p2 = head
        if p2 is None:
            return None

        while p2.next is not None:
            # swap
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1.next.next = p2
            # update
            p1 = p1.next.next
            p2 = p2.next
            if p2 is None:
                break
        return dummy.next
