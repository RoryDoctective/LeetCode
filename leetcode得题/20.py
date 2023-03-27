# 链表， delete 一个
# 双指针，end condition很恶心


# 双指针
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