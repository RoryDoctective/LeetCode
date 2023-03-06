'''

题目：之和
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        暴力破解
        '''
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+ numbers[j] == target:
                    return [i+1,j+1]



def twoSum(numbers, target):
    '''
    recursion：
    通过示例，但是未经多测试不一定对
    '''
    left = 0
    right = len(numbers) - 1

    left_num = numbers[left]
    right_num = numbers[right]

    if len(numbers) < 2:
        return [-1, -1]
    if left_num + right_num == target:
        return [left + 1, right + 1]

    temp_r = twoSum(numbers[:right], target)
    temp_l = twoSum(numbers[left + 1:], target)
    if temp_r[0] != -1:
        return temp_r
    else:
        temp_l[0] = temp_l[0] + 1
        temp_l[1] = temp_l[1] + 1
        return temp_l

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        二分查找
        '''
        length = len(numbers)
        for i in range(length-1):
            fix = numbers[i]
            num = target - fix
            left = i+1
            right = length -1
            while left <= right:
                mid = (right-left >> 1) + left
                if numbers[mid] == num:
                    return [i+1, mid+1]
                elif numbers[mid] > num:
                    right = mid -1
                else:
                    left = mid + 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        双指针
        '''
        length = len(numbers)
        left = 0
        right = length - 1

        while True:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            elif res > target:
                right -= 1
            else:
                left += 1


A = twoSum([2,3,4], 6)
B = twoSum([-1,0], -1)
print(A)
print(B)