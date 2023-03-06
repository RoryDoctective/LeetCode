# 一: list method， -1 -1 -1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notes = [x for x in ransomNote]
        pool = [x for x in magazine]
        while notes:
            word = notes[0]
            if word in pool:
                pool.remove(word)
                notes.pop(0)
            else:
                return False
        return True

# 二: string method， -1 -1 -1
# key: str.replace(old,new,几次)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notes = ransomNote
        pool = magazine
        while notes:
            word = notes[0]
            if word in pool:
                pool = pool.replace(word,"",1)
                notes = notes[1:]
            else:
                return False
        return True


# 三: set 去重 再count
# key: str.replace(old,new,几次)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notes = set(ransomNote)
        pool = magazine

        for i in notes:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

# 四: collection.Counter,
# empty set == set() -> return True
# not empty set == True -> return True
# empty set == False -> return False
# 差集： set1 - set2
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        if not(a-b):
            return True
        else:
            return False
