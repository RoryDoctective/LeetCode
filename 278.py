# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 经典二分查找例二
        left = 1
        right = n
        leftFirm = 1
        rightFirm = n

        while left <= right:
            mid = (right - left >> 1) + left
            result = isBadVersion(mid)
            if result:  # true
                rightFirm = mid
                right = mid - 1
            else:  # false
                leftFirm = mid
                left = mid + 1

        return rightFirm

# def isBadVersion(num):
#     if num > 4:
#         return True
#     else:
#         return False

# def firstBadVersion(n: int) -> int:
#     # 经典二分查找
#     left = 1
#     right = n
#     leftFirm = 1
#     rightFirm = n
#
#     while left <= right:
#         mid = (right - left >> 1) - left
#         result = isBadVersion(mid)
#         if result:  # true
#             rightFirm = mid
#             right = mid - 1
#         else:  # false
#             leftFirm = mid
#             left = mid + 1
#
#     print(leftFirm)
#     print(rightFirm)
#     return rightFirm
#
# firstBadVersion(5)