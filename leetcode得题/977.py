
'''
双指针，sort

题目：给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            num = nums[i]
            new_num = num * num
            temp.append(new_num)
        return sorted(temp)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x * x, nums)))


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        new_nums = []

        while left <= right:
            left_num = nums[left] * nums[left]
            right_num = nums[right] * nums[right]
            if left_num >= right_num:
                new_nums.append(left_num)
                left += 1
            else:
                new_nums.append(right_num)
                right -= 1
        return list(reversed(new_nums))


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        new_nums = [0] * len(nums)
        index = right

        while left <= right:
            left_num = nums[left] * nums[left]
            right_num = nums[right] * nums[right]
            if left_num >= right_num:
                new_nums[index] = left_num
                left += 1
                index -= 1
            else:
                new_nums[index] = right_num
                right -= 1
                index -= 1
        return new_nums




















