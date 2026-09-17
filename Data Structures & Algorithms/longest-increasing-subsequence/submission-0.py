class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [1] * len(nums)

        for i in range(1, len(L)):
            sub = [L[k] for k in range(i) if nums[k] < nums[i]]
            L[i] = 1 + max(sub, default=0)
        return max(L, default=0)