import heapq

'''
创建堆 2种方法
- heappush one by one 
- heapify
'''
# 1
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)
# 获取最小值不弹出
print(heap[0])

# 2
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)  # nums 改变

'''
heappop
'''
# 获取最小值,弹出
for i in range(len(nums)):
    print(heapq.heappop(nums))
print(nums)

'''
merge
'''
nums1 = [1, 2, 3, 4, 5]  # 必须排好序
nums2 = [3, 4, 5, 6, 7]  # 必须排好序
# 返回值的迭代器
nums = heapq.merge(nums1, nums2)
print(list(nums))

'''
replace
'''
nums = [2, 3, 5, 1, 54, 23, 132]
# 删除最小元素 并 加入一个元素
heapq.heapreplace(nums, 233)
print(nums)

'''
nlargest
nsmallest
'''
nums = [2, 3, 5, 1, 54, 23, 132]
# 最大/最小 得三个值
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

'''
python中的堆排序模块heapq本身不支持自定义比较函数，
(cmp_to_key 大法没有办法使用)
可以通过重写对象的__lt__方法的方式来实现自定义比较函数。
'''
# if could write directly
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

# if cannot write directly
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def __lt__(self, other):
    return self.val < other.val
ListNode.__lt__=__lt__
