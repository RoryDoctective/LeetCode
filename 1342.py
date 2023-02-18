'''
1. 位运算判断奇偶
    e.g.
    num = 22 = b"10110"
    num & 1
        = b"10110" and b"00001" = 00000
        确定最后一位是0还是1
        是1就=1
        是0就=0

    num & 1 == 1 -> 奇数
    num & 1 == 0 -> 偶数


2. 位运算表示除以 2
    e.g.
    num = 22 = b"10110"
    num >> 1
        = b"1011" = 11

    num >> 1 -> 除以2
    num >> 2 -> 除以 (2x2)


3.
 每个二进制位的1都会带来两步的代价，
 每个二进制位的0都会带来一步的代价。
 唯一特殊的是二进制最左的1最后减一为0不需要除二了，所以步数为1


 4. 海象运算符（Walrus Operator） ：=
     python 3.8 +
     即简化流程，提高运算速度
     瞬间赋值


'''


# 第一次写的：
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
        return count


# 第二次写的：
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num & 1 == 1:  # odd
                num -= 1
                count += 1
            else:  # even
                num = num >> 1
                count += 1

        return count


# 第三次
class Solution:
    def numberOfSteps(self, num: int) -> int:
        string = bin(num)[2:]
        return string.count("1") * 2 + string.count("0") * 1 - 1


# 别人的 1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(b := bin(num)[2:]) + b.count('1') - 1


# 别人的 2
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            count += (num & 1) + 1
            num >>= 1
        return max(count - 1, 0)
