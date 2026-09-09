class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force (inefficient)
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod
        # return res

        prod, zs = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zs += 1
        
        if zs > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        if zs == 1:
            for num in range(len(nums)):
                if nums[num] == 0:
                    res[num] = prod
        else: # zs == 0:
            for num in range(len(nums)):
                res[num] = prod // nums[num]

        return res
