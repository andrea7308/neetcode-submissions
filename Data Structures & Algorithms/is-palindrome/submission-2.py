class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        if not s: return True
        
        i, j = 0, len(s) - 1

        print("s:", s)
        while i < j:
            print("i:",i)
            print("j:",j)
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return s[i] == s[j]