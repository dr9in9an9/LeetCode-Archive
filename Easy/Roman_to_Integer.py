class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        cur_symbol = "I"
        for i in range(len(s) - 1, -1, -1):
            if roman[cur_symbol] > roman[s[i]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

            cur_symbol = s[i]
        return total
