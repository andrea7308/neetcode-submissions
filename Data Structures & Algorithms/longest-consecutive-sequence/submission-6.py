class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()  
        prev_num = None
        res = 0

        streak = 0
        for num in nums:
            if prev_num is None:
                prev_num = num
                continue
            if prev_num == num:
                continue
            if prev_num + 1 == num:
                streak += 1
            else:
                streak = 0
            
            prev_num = num
            res = max(streak, res)

        return res + 1