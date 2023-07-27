class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ptr1 = 0
        ptr2 = k
        vowels = 'aeiou'
        max_len = 0
        while ptr2 < len(s):
            sub = s[ptr1:ptr2]
            cur_len = 0
            for c in sub:
                if c in vowels:
                    cur_len+=1
            max_len = max(max_len, cur_len)
            ptr1 += 1
            ptr2 += 1
        return max_len