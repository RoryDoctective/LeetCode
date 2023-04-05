"""
链表：旋转链表，中等
方法：
1. get长度l，k=k mod l， 快慢指针走l-k个，再链接【自己】【超时】
2. 切嗣：连接再断开：get长度l， k=k mod l， 首尾链接，head走l-k-1个，断开链接【自己】
3. get长度l，k=k mod l， 快指针走k个，快慢指针一起走到头，断开+链接，【方法一改版，不超时间】

"""

# 1. get长度l，k=k mod l， 快慢指针走l-k个，再链接【自己】【超时】
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 双指针
        # get length
        length = 0
        p1 = head
        while p1 is not None:
            length += 1
            p1 = p1.next

        # initial
        if length == 0:
            return None
        if length == 1:
            return head

        # dif
        dif = k % length
        if dif == 0:
            return head

        # rotate
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        temp = length - dif
        while temp > 0:
            p2 = p2.next
            temp -= 1

        while p2.next is not None:
            p1.next = p2.next
            p1 = p1.next
            p2 = p2.next
        p1.next = head
        return dummy.next


# 2. 切嗣：连接再断开：get长度l， k=k mod l， 首尾链接，head走l-k-1个，断开链接【自己】
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 切嗣，连接再断开
        # make a ring, stop at the right time

        if not head or not head.next:
            return head

        # + get length
        length = 0
        p1 = head
        while True:
            length += 1
            if p1.next is None:
                break
            p1 = p1.next

        # dif
        dif = k % length
        if dif == 0:
            return head

        # 连接
        p1.next = head

        # rotate
        temp = length - dif - 1
        while temp > 0:
            head = head.next
            temp -= 1

        hold = head.next
        head.next = None
        return hold


# 3. get长度l，k=k mod l， 快指针走k个，快慢指针一起走到头，断开+链接，【方法一改版，不超时间】
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 双指针
        if not head or not head.next:
            return head

        # get length
        length = 0
        p1 = head
        while p1 is not None:
            length += 1
            p1 = p1.next

        # dif
        dif = k % length
        if dif == 0:
            return head

        # rotate
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        temp = dif
        # 快指针先走
        while temp > 0:
            p2 = p2.next
            temp -= 1
        # 一起走
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        # 断开
        hold = p1.next
        p1.next = None
        # 链接
        p2.next = head

        return hold



