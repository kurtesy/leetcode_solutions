# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = ListNode()
        ans = res
        while l1 != None or l2!=None:
            a=0
            b=0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            c = a+b+carry
            curVal = c%10
            carry = c/10
            newNode = ListNode(curVal)
            res.next = newNode
            res = res.next
            # print(newNode, ans)
        if carry > 0:
            newNode = ListNode(carry)
            res.next = newNode
        return ans.next