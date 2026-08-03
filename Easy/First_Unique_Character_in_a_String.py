class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            is_unique = True
            string_to_check = s[0: i] + s[i+1: len(s)]
            for l in string_to_check:
                if s[i] == l:
                    is_unique = False
                if not is_unique:
                    break
                
            if is_unique:
                return i
        return -1
