'''
idea: 局部反转，整体反转
题目：轮转[int]

'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        整体 swap 而已
        '''
        if k >= len(nums):
            k = k%len(nums)
        temp = nums[len(nums)-k:]
        nums[k:len(nums)] = nums[:len(nums)-k]
        nums[:k] = temp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        观察规律，局部反转x2，整体反转x1
        """
        if k >= len(nums):
            k = k % len(nums)

        length = len(nums)
        # left: 0 - len-k
        nums[0:length - k] = nums[length - k - 1::-1]
        # right : len-k - len
        nums[length - k: length] = nums[length - 1:length - k - 1:-1]
        # overall
        nums[:] = nums[::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        利用切片
        """
        if k >= len(nums):
            k = k % len(nums)

        nums[:] = nums[len(nums) - k:len(nums)] + nums[:len(nums) - k]



