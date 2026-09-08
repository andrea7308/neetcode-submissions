class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s) != len(t):
            return False

        for i in s:
            map[i] = map.get(i, 0) + 1

        for j in t:
            if map.get(j, 0) == 0:
                return False
            map[j] -= 1

        return True