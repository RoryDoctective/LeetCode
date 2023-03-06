'''

经典二分查找

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (right - left >> 1) + left
            print(mid, left, right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 经典二分查找
        left = 1
        right = n
        leftFirm = 1
        rightFirm = n

        while left <= right:
            mid = (right - left >> 1) - left
            result = isBadVersion(mid)
            if result:  # true
                rightFirm = mid
                right = mid - 1
            else:  # false
                leftFirm = mid
                left = mid + 1

        print(leftFirm)
        print(rightFirm)
        return rightFirm