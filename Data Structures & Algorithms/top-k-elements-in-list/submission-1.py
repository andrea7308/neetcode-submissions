class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # brute force
        # freq = {}

        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1

        # c = 0
        # lst = []

        # while c < k:
        #     maxc = max(freq, key=freq.get)
        #     lst.append(maxc)
        #     freq.pop(maxc)
        #     c+= 1

        # return lst


        # optimized
        freq = {}
        heap = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res