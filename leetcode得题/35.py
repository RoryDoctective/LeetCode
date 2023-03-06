# 平平无奇二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right-left >> 1) + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: # > target
                right = mid - 1
        return left
