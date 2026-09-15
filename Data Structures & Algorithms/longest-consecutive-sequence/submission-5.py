class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        curr_count = 0
        sorted_nums = sorted(nums)  
        prev_num = None
        counts = []

        if not nums: return 0

        for num in sorted_nums:
            if prev_num is None:
                prev_num = num
                continue
            if prev_num == num:
                continue
            if prev_num + 1 == num:
                curr_count += 1
            else:
                if curr_count != 0: counts.append(curr_count)
                curr_count = 0
            
            prev_num = num

        if not counts: return curr_count + 1
        else: return max(max(counts), curr_count) + 1