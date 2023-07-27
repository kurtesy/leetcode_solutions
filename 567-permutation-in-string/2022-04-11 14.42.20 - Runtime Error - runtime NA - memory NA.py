class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        temp = {}
        for i in s1:
            if i in freq:
                freq[i]+=1
                temp[i]+=1
            else:
                freq[i]=1
                temp[i]=1
        left = 0
        right = 0
        while left < len(s2):
            char = s2[right]
            if char in freq:
                freq[char]-=1
                right+=1
            else:
                if sum(freq.values()) == 0:
                    return True
                freq = {k: v for k,v in temp.items()}
                left=right+1
                right+=1
            print(freq,left,right, char)
        return False
        
            
        