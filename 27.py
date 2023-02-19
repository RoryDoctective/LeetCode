# 1 记住char，删除,下一个char
# 用了list.pop()
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        memo = None
        i = 0
        while i < len(nums):
            char = nums[i]
            if memo == char:
                nums.pop(i)
            else:
                memo = char
                i+=1

# 2. 快慢指针
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 123 left
        # 快慢指针
        '''
        nums = [ 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        0 left 0 right 1 1 1 2 2 3 3 4
        0 1 2 3 4 left 0 1 1 2 3 right
        0 1 2 left 0 1 1 2 2 3 right 3 4
        观察， 开悟
        '''
        left = 0
        right = 1
        n = len(nums)
        while right < n:
            if nums[left] == nums[right]:
                pass
            else:
                left +=1
                nums[left], nums[right] = nums[right] ,nums[left]
            right += 1
        return left+1