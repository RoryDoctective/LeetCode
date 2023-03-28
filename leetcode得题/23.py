'''
链表，困难
方法
    1. 比较器，硬写
    2. 堆：记录node指针 or 记录所有node得val
    3. 暴力：全部倒出来，排序，再连回去
    4. merge sort 改版 = merge + divide，merge: l1 and l2, divide: 0-100 to 00,11,22,...100100
    5. 顺序merge
'''

# merge sort 改版，循序merge
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge sort 改版，merge l1 and l2.
        # merge 2 lists
        def merge(l1, l2):
            p1 = p2 = ListNode(-1, None)
            while l1 and l2:
                if l1.val <= l2.val:
                    p2.next = l1
                    l1 = l1.next
                    p2 = p2.next
                else:
                    p2.next = l2
                    l2 = l2.next
                    p2 = p2.next
            p2.next = l1 if l1 else l2
            return p1.next

        if not lists:
            return None

        accum = None
        for i in lists:
            accum = merge(accum, i)
        return accum


# merge sort 改版，merge l1 and l2.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge sort 改版，merge l1 and l2.
        # merge 2 lists
        def merge(l1, l2):
            p1 = p2 = ListNode(-1, None)
            while l1 and l2:
                if l1.val <= l2.val:
                    p2.next = l1
                    l1 = l1.next
                    p2 = p2.next
                else:
                    p2.next = l2
                    l2 = l2.next
                    p2 = p2.next
            p2.next = l1 if l1 else l2
            return p1.next

        # divide and concur
        def together(L, R):
            if L == R:
                return lists[L]
            mid = (R - L >> 1) + L
            left = together(L, mid)
            right = together(mid + 1, R)
            return merge(left, right)

        if not lists:
            return None
        final = together(0, len(lists) - 1)
        return final


# 堆，用heapq,记录每一个value
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 堆，用heapq,record value
        import heapq

        # push all value into heapq
        heap = []
        for i in lists:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next

        # setting dummy
        p1 = p2 = ListNode(-1, None)

        # take one
        while heap:
            n = heapq.heappop(heap)
            p2.next = ListNode(n, None)
            p2 = p2.next
        return p1.next


# 堆，用heapq, 堆记录每一个node得指针
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 堆，用heapq
        import heapq

        # make comparable
        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        # push into heapq
        heap = []
        for i in lists:
            if i is not None:
                heapq.heappush(heap, i)

        # setting dummy
        p1 = p2 = ListNode(-1, None)

        # take one put one
        while heap:
            n = heapq.heappop(heap)
            p2.next = n
            p2 = p2.next
            if n.next is not None:
                heapq.heappush(heap, n.next)
        return p1.next


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