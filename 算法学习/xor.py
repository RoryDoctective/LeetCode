'''
list of [int], 里面有正整数，所有数字都出现了偶数次，只有**一个数字a**出现了奇数次，请找到它：

- 把所有的int都异或起来
- 因为 N ^ N = 0, N ^ 0 = N
- 最后只会剩下那个a

'''

l = [11,11,11,66,66,44,4,44,4]
a = 0
for i in range(len(l)):
    a = a ^ l[i]
print(a)

'''
list of [int], 里面有正整数，所有数字都出现了偶数次，只有**两个数字a和b**分别出现了奇数次，请找到它：

- 把所有的int都异或起来 = a ^ b = c
- 需要找到 a or b 其中的一个
- 因为 a != b, 所以 a^b != 0, 所以c其中一个位数（假设这个位数是32位中的第8位）一定是一个0一个是1
- 所以我们可以把list中的所有数字分成2波
  - 一波A第8位是0， 一波B第8位是1
- 把A里面的所有数都异或起来 = a或者b的值，say = b
- c^b = a ^ b ^ b = a ^ 0 = a

'''

l = [11, 11, 11, 66, 66, 44, 4, 44, 4, 5]

# find a ^ b
c = 0
for i in range(len(l)):
    c = c ^ l[i]

# find c 右数第几位是 1
n = c & (~c + 1)

# find A and B
A = []

for i in range(len(l)):
    # 这里不可以 == 1， 应该是 == n, 那个位数为1
    if (n & l[i]) == 0:  # 那个位数是0
        A.append(l[i])

# find a
a = 0
for i in range(len(A)):
    a = a ^ A[i]

# find b
b = c ^ a

print(a, b)