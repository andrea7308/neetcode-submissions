class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(digit) for digit in digits)
        s = int(s)
        new = str(s + 1)
        res = []
        for c in new:
            res.append(c)
        
        return res