class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        map = {}

        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1

        return duplicate
