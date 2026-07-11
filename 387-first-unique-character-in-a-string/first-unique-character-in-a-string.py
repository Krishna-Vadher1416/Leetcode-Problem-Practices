class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen = {}

        for i in s :
            seen[i] = seen.get(i,0) + 1

        for index , char in enumerate(s) :
            if seen[char] == 1:
                return index

        return -1
        