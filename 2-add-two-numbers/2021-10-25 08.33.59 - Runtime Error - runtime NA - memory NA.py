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
        cur1 = l1
        while cur1!=None and l2!=None:
            a = cur1.val
            b = l2.val
            c = a+b+carry
            # print(a,b,c,carry)
            curVal = c%10
            carry = int(c/10)
            cur1.val = curVal
            cur1 = cur1.next
            l2 = l2.next
        if cur1:
            prev = None
            while cur1!=None:
                a = cur1.val
                c = a+carry
                # print(a,b,c,carry)
                curVal = c%10
                carry = int(c/10)
                cur1.val = curVal
                prev = cur1
                cur1 = cur1.next
        if carry > 0:
            print('cur1', cur1, carry)
            newNode = ListNode(carry)
            prev.next = newNode
        return l1
            
        