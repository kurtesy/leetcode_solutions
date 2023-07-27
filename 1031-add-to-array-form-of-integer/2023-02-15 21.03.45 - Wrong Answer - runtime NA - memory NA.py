class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        carry = 0
        ptr = len(num)-1
        res = []
        while ptr >= 0:
            op1 = k%10
            k=k//10
            op2 = num[ptr]
            _sum = op1+op2+carry
            carry = _sum//10
            res = [_sum%10]+res
            ptr-=1
        if carry > 0:
            res = [carry]+res
        return res