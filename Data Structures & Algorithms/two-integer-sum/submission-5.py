class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []

        # optimized solution
        A = []

        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()

        i, j = 0, len(nums) -1 

        while i < j:
            cur = A[i][0] + A[j][0]

            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            
            elif cur < target:
                i += 1
            
            else: # cur > target:
                j -= 1
        
        return []


