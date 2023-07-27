class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for i in s1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        w, match = len(s1), 0     

        for i in range(len(s2)):
            if s2[i] in freq:
                if not freq[s2[i]]: match -= 1
                freq[s2[i]] -= 1
                if not freq[s2[i]]: match += 1

            if i >= w and s2[i-w] in freq:
                if not freq[s2[i-w]]: match -= 1
                freq[s2[i-w]] += 1
                if not freq[s2[i-w]]: match += 1

            if match == len(freq):
                return True
        return False
        
            
        