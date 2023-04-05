"""
链表：升序排列得链表删除重复元素-中等

方法：
1. 递归，每次处理一个【自己】
2. 迭代， 双指针，分清：【自己】
    1. 下一个是None
    2. 下一个是第一个val
    3. 下一个是第二及以上的val
3. 迭代， 单指针【别人】

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. 递归，每次处理一个【自己】
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        # END：empty or just one node
        if not head or not head.next: # [] 和 [0]
            return head

        p1 = head
        memo = p1.val
        count = 0

        while p1.next and p1.val == memo:
            p1 = p1.next
            count += 1

        if count == 1 and p1.val != memo:  # [0,1]
            head.next = self.deleteDuplicates(p1)
            return head

        if p1.val != memo:  # [0,0,0,1]
            return self.deleteDuplicates(p1)

        if p1.val == memo:  # [0,0,E]
            return None


# 2. 迭代， 双指针，分清：【自己】
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty or just one node
        if not head or not head.next:
            return head

        # add helper
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy

        # 下一个不是空
        while p1.next is not None:
            count = 0
            # 快指针移动
            while p2.next and p1.next.val == p2.next.val:  # 下一个不是空且val一样
                p2 = p2.next
                count += 1
            # only 1, jump
            if count == 1:  # 比如：[1,2,3],1,2,3都是不用删的
                p1 = p2
            else:
                # 比如：[1,1,2,3],1是用删的
                # 比如：[],以下操作不影响
                p1.next = p2.next  # delete
                p2 = p1

        return dummy.next


# 3. 迭代， 单指针【别人】
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代
        # [], [0]
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy

        while p1.next and p1.next.next:
            val = p1.next.val
            if p1.next.next.val == val:  # same
                while p1.next and p1.next.val == val:
                    p1.next = p1.next.next
            else:
                p1 = p1.next
        return dummy.next





