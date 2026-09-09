class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        c = 0
        lst = []

        while c < k:
            maxc = max(freq, key=freq.get)
            lst.append(maxc)
            freq.pop(maxc)
            c+= 1

        return lst