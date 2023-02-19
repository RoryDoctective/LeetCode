# 一：错，因为剩下的顺序变了

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        selection sort -> 错，因为剩下的顺序变了
        """
        index = len(nums) - 1
        for i in reversed(range(len(nums))):  # n-1 -> 0
            if nums[i] == 0:
                nums[i], nums[index] = nums[index], nums[i]
                index = index - 1


# 二
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        idea: bubble sort -> 但是超时了
        """
        for i in range(len(nums)):  # 0 -> n-1
            for j in range(len(nums) - i - 1):  # 0-> n-1 - i
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


# 3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        idea: bubble sort + count (提前停止) -> 还是超时啦
        """
        num = nums.count(0)
        for i in range(len(nums)):  # 0 -> n-1
            if num == 0:
                break
            for j in range(len(nums) - i - 1):  # 0-> n-1 - i
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            num -= 1


# 4
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        idea: 单纯的删一个加一个
        """
        num = nums.count(0)
        for i in range(num):
            nums.remove(0)
            nums.append(0)


# 5
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        idea: 所有非零的往前挪，剩下的零补齐
        """
        n = len(nums)
        p = 0
        count = 0
        for i in range(n):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1
            else:
                count += 1
        for i in range(n - count, n):
            nums[i] = 0


# 6 快慢指针
# 742642 right 00000 left 9084050
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # 6 快慢指针
        # [742642 left 00000 right 9084050]
        """
        n = len(nums)
        right = left = 0
        while right < n:
            # 零不换，不等于零就换
            if nums[right] != 0:  # swap
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            # always 
            right += 1
