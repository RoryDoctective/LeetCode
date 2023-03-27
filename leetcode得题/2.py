# 链表
# 两个链表相加
# 方法：
#   1. 直接写
#   2. 递归
#   3. 双指针
# 学到了：
#   1. dummy = ListNode(), p=dummy, return dummy.next 得方法保留头
#   2. carry = sum//10; val = sum %10

# 别人写的双指针（比我的简单多了）
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        p1 = l1
        p2 = l2
        carry = 0
        while p1 or p2:
            first, second = 0, 0
            if p1:
                first = p1.val
                p1 = p1.next
            if p2:
                second = p2.val
                p2 = p2.next
            sums = first + second + carry
            carry = sums // 10
            val = sums % 10
            p.next = ListNode(val, None)
            p = p.next

        if carry:
            p.next = ListNode(carry, None)
        return dummy.next


# 别人的递归： 建议再写一遍自己想不到
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val = l1.val + l2.val
        if l1.val > 9:
            # // 整除
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            # % 取余
            l1.val = l1.val % 10

        l1.next = self.addTwoNumbers(l1.next, l2.next)

        return l1


# 自己写的垃圾： 直接写
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        memo = 0
        res = l1
        flag_2 = True
        flag_3 = True
        while flag_2 and flag_3:
            l1_digit = l1.val
            l2_digit = l2.val
            # 前一次得进位
            add_digit = l1_digit + l2_digit + memo
            # 这一次得进位
            if add_digit > 9:
                add_digit = add_digit - 10
                memo = 1
            else:
                memo = 0

            # record
            l1.val = add_digit
            if l1.next is None:
                flag_2 = False

            if l2.next is None:
                flag_3 = False

            # new
            if flag_2:
                l1 = l1.next
            if flag_3:
                l2 = l2.next

        if not flag_3 and not flag_2:
            if memo == 1:
                l1.next = ListNode(1, None)

        elif not flag_2:
            # copy untill end
            while l2:
                # 前一次得进位
                l2.val = l2.val + memo
                # 这一次得进位
                if l2.val > 9:
                    l2.val = l2.val - 10
                    memo = 1
                else:
                    memo = 0

                l1.next = ListNode(l2.val, None)
                l1 = l1.next
                l2 = l2.next
            if memo == 1:
                l1.next = ListNode(1, None)

        else:
            # not l2:
            # copy untill end
            flag = True
            while flag:
                # 前一次得进位
                l1.val = l1.val + memo
                # 这一次得进位
                if l1.val > 9:
                    l1.val = l1.val - 10
                    memo = 1
                else:
                    memo = 0
                if l1.next is None:
                    flag = False
                    break
                l1 = l1.next
            if memo == 1:
                l1.next = ListNode(1, None)

        return res

