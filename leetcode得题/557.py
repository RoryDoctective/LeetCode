'''
双指针
python操作

反转字符串中得单词
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        双指针，手写
        '''

        res = ""
        l = s.split(" ")
        for temp in l:
            ss = list(temp)
            left = 0
            right = len(ss) - 1
            while left <= right:
                ss[left], ss[right] = ss[right], ss[left]
                left += 1
                right -= 1
            res = res + "".join(ss) + " "
        return res[:-1]

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        炫酷 python
        '''
        return " ".join(x[::-1] for x in s.split(" "))

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        纯手写实现 s.split 和 slice
        很慢
        '''
        left = 0
        right = 1
        final = ''
        s = s+" "
        while right < len(s):
            if s[right] == ' ':
                # left <-> right-1 is a word
                temp = right -1
                while temp >= left:
                    final = final + s[temp]
                    temp -= 1
                final = final + ' '
                left = right+1
                right = right+2
            else:
                right += 1
        return final[:-1]

# A = reverseWords("Let's take LeetCode contest")
# print(A)