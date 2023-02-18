class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        accum = 0
        for i in range(len(nums)):
            num = nums[i]
            accum += num
            res.append(accum)
        return res
