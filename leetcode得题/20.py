'''
链表， delete 一个 node
方法：
    1. 双指针，end condition很恶心
    2. 数长度
    3. 栈/queue 【最不好】
'''


# 双指针 -》 自己写的很麻烦
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针
        dummy = ListNode(-1, head)
        p1 = dummy  # 0
        p2 = p1  # n-1 say n=2, then p2 = 2
        for _ in range(n):
            p2 = p2.next

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        # print(p1.val)
        # print(p2.val)


        if p1.next.next == None:
            '''处理p1=4, p2=5'''
            p1.next = None
            if p1.val == -1:
                '''处理p1=-1, p2=1'''
                return None
        else:
            p1.next = p1.next.next
            if p1.val == -1:
                '''处理p1=-1, p2=5'''
                return head.next

        return head


# 双指针，化简版本
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针，简单一点
        dummy = ListNode(-1,head)
        p1 = dummy
        p2 = head
        for i in range(n):
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next


# 数长度
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # get length
        length = getLength(head)
        dummy = ListNode(-1, head)
        p = dummy
        # before_node = length - n
        for _ in range(1, length - n + 1):  # [1 - length-n ]
            p = p.next

        p.next = p.next.next
        return dummy.next


# 用栈。
# add all then pop n, the last is the point
# ps: List all the node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Stack/栈
        stack = []
        dummy = ListNode(-1, head)
        p = dummy
        while p:
            stack.append(p)
            p = p.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next
