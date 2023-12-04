class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sub_size = 3
        result = -1
        prev = num[0]
        sub = prev
        for n in num[1:]:
            if prev == n:
                sub+=n
            else:
                if len(sub) >= sub_size:
                    result = max(int(sub[0]),result)
                sub=n
            prev=n
        print(result)
        if len(sub) >= sub_size:
            result = max(int(sub[0]),result)
        print(result,sub)
        if result == -1:
            return ''
        return str(result)*sub_size