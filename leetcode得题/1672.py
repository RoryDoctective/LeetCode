
# 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ = 0
        for i in range(len(accounts)):
            max_ = max(sum(accounts[i]), max_)
        return max_

# 2
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)

# 3
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
