"""
链表：升序排列得链表删除重复元素

方法：
1. 利用set去重，双指针删除链表【自己】
2. 利用升序排列，一样的元素一定连在一起，双指针删除链表【自己】
3. 利用升序排列，一样的元素一定连在一起，单指针删除链表【自己】
4. 递归，每次处理一个

"""

# 1. 利用set去重，双指针删除链表【自己写得】
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = set({})
        p1 = head
        temp.add(p1.val)
        p2 = head.next
        while p2 is not None:
            len1 = len(temp)
            temp.add(p2.val)
            len2 = len(temp)
            if len1 == len2:
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
        return head


# 2. 利用升序排列，一样的元素一定连在一起，，双指针删除链表【自己】
# 利用memo记录，慢，内存小
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p1 = head
        memo = p1.val
        p2 = head.next

        while p2 is not None:
            if p2.val == memo:
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
                memo = p1.val
        return head
# 不利用memo记录，快，内存大
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p1 = head
        p2 = head.next

        while p2 is not None:
            if p2.val == p1.val:
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
        return head


# 3. 利用升序排列，一样的元素一定连在一起，单指针删除链表【自己】
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p1 = head

        while p1.next is not None:
            if p1.next.val == p1.val:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        return head



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        if head is None:
            return None
        if head.next is None:
            return head

        if head.val == head.next.val:
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head