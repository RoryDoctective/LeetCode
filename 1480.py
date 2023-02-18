class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        accum = 0
        for i in range(len(nums)):
            num = nums[i]
            accum += num
            res.append(accum)
        return res


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums
