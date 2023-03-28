'''
链表，困难
方法
    1. 比较器，硬写
    2. 堆
    3. 暴力：全部倒出来，排序，再连回去
'''


# 暴力：全部倒出来，排序，再连回去
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        bucket = []
        for i in range(len(lists)):
            while lists[i]:
                bucket.append(lists[i].val)
                lists[i] = lists[i].next
        bucket.sort()
        dummy = ListNode(-1, None)
        p1 = dummy
        p2 = p1
        for i in range(len(bucket)):
            p2.next = ListNode(bucket[i], None)
            p2 = p2.next
        return p1.next


# 自己写的，化简了，对了但是超时了
from functools import cmp_to_key
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 迭代
        def cmp(node1, node2):
            if node1 == None and node2 == None:
                return 0
            if node1 == None:
                return 1
            if node2 == None:
                return -1
            return node1.val - node2.val

        dummy = ListNode(-1, None)
        p1 = dummy
        p2 = dummy

        if len(lists) == 0:
            return None

        while True:
            lists.sort(key=cmp_to_key(cmp))
            if lists[0] is None:
                break

            p2.next = lists[0]
            p2 = p2.next
            lists[0] = lists[0].next

        return p1.next

# 自己写的，比较繁琐，对了但是超时了
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 迭代
        def cmp(node1, node2):
            return node1.val - node2.val

        dummy = ListNode(-1, None)
        p1 = dummy
        p2 = dummy

        record = []
        for i in range(len(lists)):
            if lists[i] == None:
                record.append(i)
        for i in reversed(record):
            del lists[i]
        if len(lists) == 0:
            return None

        while True:
            lists.sort(key=cmp_to_key(cmp))
            p2.next = lists[0]
            p2 = p2.next

            if lists[0] is None:
                break

            if lists[0].next is None:
                del lists[0]
            else:
                lists[0] = lists[0].next

            if len(lists) == 0:
                break

        return p1.next