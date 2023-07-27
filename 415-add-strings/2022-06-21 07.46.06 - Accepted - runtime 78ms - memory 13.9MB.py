class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n,m = len(num1), len(num2)
        i = n-1
        j = m-1
        res = ''
        c = 0
        while i>=0 or j>=0:
            if i>=0:
                y=int(num1[i])
            else:
                y=0
            if j>=0:
                z=int(num2[j])
            else:
                z=0
            x = y+z+c
            c = x//10
            x=x%10
            res=str(x)+res
            i-=1
            j-=1
        if c>0:
            res=str(c)+res
        return res
        