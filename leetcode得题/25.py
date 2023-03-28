# K 个一组翻转链表

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 迭代
        p1 = dummy = ListNode(-1, head)
        p2 = head
        flag = True
        while True:
            # stopping condition
            temp = p2
            for i in range(k):
                if temp is None:
                    flag = False
                temp = temp.next
            if flag == False:
                break

            # swap
            # step 1
            temp = p1
            for i in range(k):
                temp = temp.next
            p1.next = temp
            # step 2
            temp2 = p2.next
            p2.next = temp.next
            # reverse
            temp3 = temp2.next  # memo
            for i in range(k):
                temp2.next = p2  # reverse
                p2 = temp2  # step
                temp2 = temp3
                temp3 = temp3.next  # memo
            # update p1 nd p2
            p1 = p2.next
            p2 = p2.next.next
        return dummy.next