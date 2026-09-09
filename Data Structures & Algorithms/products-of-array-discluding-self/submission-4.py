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


        for i, c in enumerate(nums):
            if zs == 1:
                if c: res[i] = 0
                else: res[i] = prod
            else: # zs = 0:
                res[i] = prod // c

        return res
