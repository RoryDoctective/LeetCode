'''
链表，merge
方法：
    1.递归

'''

# 我自己写得递归 = 跟官方写得一样
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 我自己写得迭代
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代
        dummy = ListNode(-1, None)
        p1 = dummy
        p2 = dummy

        while l1 or l2:
            first, second = 101, 101
            if l1:
                first = l1.val
            if l2:
                second = l2.val

            if first <= second and first < 101:
                p2.next = l1
                p2 = p2.next
                l1 = l1.next
            if first >= second and second < 101:
                p2.next = l2
                p2 = p2.next
                l2 = l2.next
        return p1.next


# 答案得迭代
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代
        dummy = ListNode(-1, None)
        p1 = dummy
        p2 = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                p2.next = l1
                l1 = l1.next
            else:
                p2.next = l2
                l2 = l2.next
            p2 = p2.next

        p2.next = l1 if l2 is None else l2

        return p1.next







